from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from .pages.input_page import InputPage
from .pages.results_page import ResultsPage
import os

class MainWindow(QMainWindow):
    """Main window for the OpenModelica Simulator application."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenModelica Simulator")
        self.setMinimumSize(800, 600)
        self.resize(1200, 800)
        self.worker=None
        
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        self.selected_format = None 
        self.is_default = False 
        self.path=None
        
        self.input_page = InputPage(self)  
        self.results_page = ResultsPage(self)
        
        
        self.stacked_widget.addWidget(self.input_page)
        self.stacked_widget.addWidget(self.results_page)

        self.stacked_widget.currentChanged.connect(self.on_page_changed)

    def go_to_results_page(self):
        """Switch to the results page."""
        self.stacked_widget.setCurrentIndex(1)
        

    def go_to_input_page(self):
        """Switch back to the input page."""
        self.stacked_widget.setCurrentIndex(0)

    def on_page_changed(self,index):
        if index==1:
            self.results_page.set_status_text(f"Result are also available in {os.path.dirname(self.path)}")