from pathlib import Path
from typing import Union, Tuple


class ValidationError(Exception):
    """Custom exception for validation errors during input validation."""
    pass


def validate_inputs(
    exe_path: str,
    start_time: str,
    stop_time: str
) -> bool:
    """Validate user inputs for OpenModelica simulation.
    
    Args:
        exe_path: Path to the executable file.
        start_time: Start time for simulation as string.
        stop_time: Stop time for simulation as string.
    
    Returns:
        bool: True if all validations pass.
    
    Raises:
        FileNotFoundError: If no executable is selected or file doesn't exist.
        ValidationError: If any validation check fails.
    
    Notes:
        Time constraints:
        - Start time must be >= 0 and < 5
        - Stop time must be < 5
        - Start time must be less than stop time
    """
    if not exe_path:
        raise FileNotFoundError("Please select an executable file.")
        
    if not Path(exe_path).exists():
        raise ValidationError(f"Executable not found: {exe_path}")
    
    if not start_time or not stop_time:
        raise ValidationError("Both start time and stop time must be provided.")
    
    try:
        start: float = float(start_time)
        stop: float = float(stop_time)
    except ValueError:
        raise ValidationError("Start time and stop time must be valid numbers.")
    
    _validate_time_constraints(start, stop)
    
    return True


def _validate_time_constraints(start: float, stop: float) -> None:
    """Validate time constraints for the simulation.
    
    Args:
        start: Start time as float.
        stop: Stop time as float.
    
    Raises:
        ValidationError: If any time constraint is violated.
    """
    if start < 0:
        raise ValidationError("Start time must be greater than or equal to 0.")
    
    if start >= 5:
        raise ValidationError("Start time must be less than 5.")
        
    if stop >= 5:
        raise ValidationError("Stop time must be less than 5.")
        
    if start >= stop:
        raise ValidationError("Start time must be less than stop time.")