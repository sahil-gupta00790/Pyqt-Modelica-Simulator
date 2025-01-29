from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

from ..widgets.file_input import FileInput
from ..widgets.time_input import TimeInput
from ..widgets.format_selector import FormatSelector
from ..styles import get_button_style
from utils.simulator import run_simulation
from utils.validator import ValidationError, validate_inputs
from ..widgets.loading import run_simulation_with_loading
class InputPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  
        self.setup_ui()

    def setup_ui(self):
        """Set up the input page UI."""
        # Set window background color
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#1a1a1a"))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        # Main layout
        layout = QVBoxLayout()
        
        # Container for content
        container = QWidget()
        container.setFixedWidth(600)
        content_layout = QVBoxLayout(container)
        content_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # adding widgets
        self.file_input = FileInput()
        self.start_time = TimeInput("Start Time")
        self.stop_time = TimeInput("Stop Time")
        self.format_selector = FormatSelector()

        content_layout.addWidget(self.file_input)
        content_layout.addWidget(self.start_time)
        content_layout.addWidget(self.stop_time)
        content_layout.addWidget(self.format_selector)

        # Execute button
        self.execute_button = QPushButton("Execute Simulation")
        self.execute_button.setStyleSheet(get_button_style())
        self.execute_button.clicked.connect(self.run_executable)
        content_layout.addWidget(
            self.execute_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def run_executable(self):
        """Execute the simulation with current parameters."""
        try:
            exe_path = self.file_input.get_file_path()
            start_time = self.start_time.get_value()
            stop_time = self.stop_time.get_value()
            output_format = self.format_selector.get_selected_format()
            is_default = self.file_input.default_checkbox.isChecked()

            if validate_inputs(exe_path, start_time, stop_time):
                self.main_window.selected_format = output_format
                self.main_window.is_default = is_default  
                self.main_window.path=exe_path
                run_simulation_with_loading(exe_path, start_time, stop_time, output_format)
                self.main_window.go_to_results_page()
            
        except ValidationError as e:
            self.file_input.show_error_dialog(str(e))
        except FileNotFoundError as e:
            self.file_input.show_error_dialog(str(e))
        except Exception as e:
            self.file_input.show_error_dialog(str(e))