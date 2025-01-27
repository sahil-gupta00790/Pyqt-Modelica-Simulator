from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from .pages.input_page import InputPage
from .pages.results_page import ResultsPage

class MainWindow(QMainWindow):
    """Main window for the OpenModelica Simulator application."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenModelica Simulator")
        self.setMinimumSize(800, 600)
        self.resize(1200, 800)
        
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        
        self.input_page = InputPage(self)  
        self.results_page = ResultsPage(self)
        
        
        self.stacked_widget.addWidget(self.input_page)
        self.stacked_widget.addWidget(self.results_page)

    def go_to_results_page(self):
        """Switch to the results page."""
        self.stacked_widget.setCurrentIndex(1)

    def go_to_input_page(self):
        """Switch back to the input page."""
        self.stacked_widget.setCurrentIndex(0)