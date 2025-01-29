from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QProgressBar
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
import threading
from utils.simulator import run_simulation

class LoadingScreen(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Processing")
        # Remove the window title bar
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        # Create the layout
        layout = QVBoxLayout()
        
        # Add loading text
        self.label = QLabel("Running Simulation...")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont('Arial', 12))
        layout.addWidget(self.label)
        
        # Add progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(0)  # Indeterminate progress
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
                width: 10px;
            }
        """)
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)
        
        # Set fixed size
        self.setFixedSize(300, 100)
        
        # Center the dialog on the parent window
        if parent:
            self.move(
                parent.x() + parent.width()//2 - self.width()//2,
                parent.y() + parent.height()//2 - self.height()//2
            )

def run_simulation_with_loading(self, exe_path, start_time, stop_time, output_format):
    # Create and show loading screen
    loading_screen = LoadingScreen(self.main_window)
    loading_screen.show()
    
    def simulation_thread():
        try:
            # Run the simulation
            run_simulation(exe_path, start_time, stop_time, output_format)
            
            # Close loading screen and proceed to results
            loading_screen.accept()
            self.main_window.go_to_results_page()
        except Exception as e:
            # Handle any errors
            loading_screen.label.setText(f"Error: {str(e)}")
            loading_screen.progress_bar.setStyleSheet("""
                QProgressBar::chunk {
                    background-color: #f44336;
                }
            """)
            # Wait 2 seconds before closing on error
            QTimer.singleShot(2000, loading_screen.reject)
    
    # Start the simulation in a separate thread
    thread = threading.Thread(target=simulation_thread)
    thread.start()