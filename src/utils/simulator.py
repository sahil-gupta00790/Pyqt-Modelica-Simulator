import subprocess
from pathlib import Path
from typing import List, Optional


def run_simulation(
    exe_path: str,
    start_time: float,
    stop_time: float,
    output_format: str
) -> None:
    """Run OpenModelica simulation with specified parameters.
    
    Args:
        exe_path: Path to the executable file.
        start_time: Simulation start time in seconds.
        stop_time: Simulation stop time in seconds.
        output_format: Output file format (e.g., '.mat' or '.csv').
    
    Raises:
        FileNotFoundError: If the executable file doesn't exist.
        RuntimeError: If simulation fails or support files can't be read.
    """
    if not Path(exe_path).exists():
        raise FileNotFoundError(f"Executable not found: {exe_path}")
        
    cmd: List[str] = [
        exe_path,
        f"-override=startTime={start_time},stopTime={stop_time}",
        f"-r=result{output_format}"
    ]
    
    try:
        subprocess.run(
            cmd,
            check=True,
            cwd=Path(exe_path).parent,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        error_message: str = str(e)
        
        if "3221225477" in error_message:
            raise RuntimeError(
                "Error: Cannot read support files in this directory"
            )
        raise RuntimeError(f"Simulation failed: {e}")