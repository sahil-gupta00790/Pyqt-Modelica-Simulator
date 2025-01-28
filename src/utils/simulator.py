import subprocess
from pathlib import Path

def run_simulation(exe_path: str, start_time: float, stop_time: float, output_format: str) -> None:
    """Run OpenModelica simulation with specified parameters."""
    if not Path(exe_path).exists():
        raise FileNotFoundError(f"Executable not found: {exe_path}")
        
    cmd = [
        exe_path,
        f"-override=startTime={start_time},stopTime={stop_time}",
        f"-r=result{output_format}"
    ]
    
    try:
        result = subprocess.run(cmd, check=True, cwd=Path(exe_path).parent, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        error_message=str(e)
        
        if "3221225477." in error_message:
            raise RuntimeError(f"Error: Can not read support files in this directory")
        else:
            raise RuntimeError(f"Simulation failed: {e}")
