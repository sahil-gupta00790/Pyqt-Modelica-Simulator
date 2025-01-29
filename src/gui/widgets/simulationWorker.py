from PyQt6.QtCore import QThread, pyqtSignal
from utils.simulator import run_simulation

class SimulationWorker(QThread):
    finished = pyqtSignal()
    error = pyqtSignal(str)
    
    def __init__(self, exe_path, start_time, stop_time, output_format):
        super().__init__()
        self.exe_path = exe_path
        self.start_time = start_time
        self.stop_time = stop_time
        self.output_format = output_format
        
    def run(self):
        try:
            run_simulation(
                self.exe_path, 
                self.start_time, 
                self.stop_time, 
                self.output_format
            )
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))