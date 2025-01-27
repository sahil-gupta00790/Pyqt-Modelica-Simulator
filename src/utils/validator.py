from pathlib import Path

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_inputs(exe_path: str, start_time: str, stop_time: str) -> bool:
    """
    Validate user inputs for OpenModelica simulation.
    Raises ValidationError with specific error message if validation fails.
    """
    # Check if executable path is provided
    if not exe_path:
        raise FileNotFoundError("Please select an executable file.")
        
    # Check if executable exists
    if not Path(exe_path).exists():
        raise ValidationError(f"Executable not found: {exe_path}")
    
    # Check if times are provided
    if not start_time or not stop_time:
        raise ValidationError("Both start time and stop time must be provided.")
    
    try:
        start = float(start_time)
        stop = float(stop_time)
    except ValueError:
        raise ValidationError("Start time and stop time must be valid numbers.")
    
    # Check time constraints
    if start < 0 :
        raise ValidationError("Start time must be greater than or equal to 0.")
    elif start >= 5:
        raise ValidationError("Start time must be less than 5.")
    if stop >= 5:
        raise ValidationError("Stop time must be less than 5.")
    if start >= stop:
        raise ValidationError("Start time must be less than stop time.")
    
    return True