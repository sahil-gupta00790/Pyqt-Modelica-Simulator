from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

from ..styles import get_button_style

class ResultsPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # Store reference to main window for navigation
        self.setup_ui()

    def setup_ui(self):
        """Set up the results page UI."""
        # Set window background color
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#1a1a1a"))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        
        layout = QVBoxLayout()
        
        # Add your results widgets here
        results_label = QLabel("Simulation Results")
        results_label.setStyleSheet("color: white; font-size: 24px;")
        layout.addWidget(results_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Back button
        back_button = QPushButton("Back to Input")
        back_button.setStyleSheet(get_button_style())
        back_button.clicked.connect(self.main_window.go_to_input_page)
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(layout)