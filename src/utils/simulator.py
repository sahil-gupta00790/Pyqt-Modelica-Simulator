import subprocess
from pathlib import Path

def run_simulation(exe_path: str, start_time: float, stop_time: float , output_format:str) -> None:
    """Run OpenModelica simulation with specified parameters."""
    if not Path(exe_path).exists():
        raise FileNotFoundError(f"Executable not found: {exe_path}")
        
    cmd = [
        exe_path,
        f"-override=startTime={start_time},stopTime={stop_time}",
        f"-r=result{output_format}"
    ]
    print(output_format[1:])
    try:
        subprocess.run(cmd, check=True,cwd=Path(exe_path).parent)
    except subprocess.CalledProcessError as e:
        raise (f"Simulation failed: {e}")