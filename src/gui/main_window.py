from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                           QPushButton, QFileDialog, QLineEdit, QLabel,
                           QMessageBox, QGroupBox, QDoubleSpinBox, QComboBox)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
from utils.validator import validate_inputs, ValidationError
from utils.simulator import run_simulation

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenModelica Simulator")
        self.setMinimumSize(800, 600)
        self.resize(1200, 800)
        self.setup_ui()

    def get_dark_theme_style(self):
        return """
            QGroupBox {
                margin-top: 10px;
                padding: 15px;
                background-color: #2d2d2d;
                border: 1px solid #3d3d3d;
                border-radius: 5px;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
            }
            QLineEdit, QDoubleSpinBox, QComboBox {
                background-color: #383838;
                border: 1px solid #3d3d3d;
                border-radius: 4px;
                padding: 5px;
                color: #ffffff;
            }
            QLineEdit:focus, QDoubleSpinBox:focus, QComboBox:focus {
                border: 1px solid #0078d4;
            }
            QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {
                background-color: #444444;
            }
            QComboBox::drop-down {
                border: none;
                background-color: #444444;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #ffffff;
            }
            QComboBox:on {
                border: 1px solid #0078d4;
            }
            QComboBox QAbstractItemView {
                background-color: #383838;
                color: #ffffff;
                selection-background-color: #0078d4;
            }
        """

    def get_button_style(self):
        return """
            QPushButton {
                background-color: #0078d4;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 14px;
                min-width: 120px;
                max-width: 200px;
            }
            QPushButton:hover {
                background-color: #1484d7;
            }
            QPushButton:pressed {
                background-color: #006cbd;
            }
        """

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Apply a border to the central widget
        palette = central_widget.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#1a1a1a"))
        central_widget.setAutoFillBackground(True)
        central_widget.setPalette(palette)

        # Main layout
        layout = QVBoxLayout()
        
        # Create a container widget for content with fixed width
        container = QWidget()
        container.setFixedWidth(600)
        content_layout = QVBoxLayout(container)
        content_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # File selection
        self.file_input_box = self.create_file_explorer_box()
        content_layout.addWidget(self.file_input_box)

        # Time inputs
        self.start_time_box = self.create_float_input_box("Start Time:")
        self.stop_time_box = self.create_float_input_box("Stop Time:")
        content_layout.addWidget(self.start_time_box)
        content_layout.addWidget(self.stop_time_box)

        # Dropdown menu with additional options
        self.dropdown_menu = self.create_dropdown_menu()
        content_layout.addWidget(self.dropdown_menu)

        # Execute button
        self.execute_button = QPushButton("Execute Simulation")
        self.execute_button.setStyleSheet(self.get_button_style())
        self.execute_button.clicked.connect(self.run_executable)
        content_layout.addWidget(self.execute_button)

        # Add container to main layout with alignment
        layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)
        central_widget.setLayout(layout)

    def create_file_explorer_box(self):
        box = QGroupBox("Select Executable")
        box.setStyleSheet(self.get_dark_theme_style())
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 10, 20, 10)

        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("Path to .exe file")
        browse_button = QPushButton("Browse")
        browse_button.setStyleSheet(self.get_button_style())
        browse_button.setFixedWidth(100)
        browse_button.clicked.connect(self.select_file)

        layout.addWidget(self.file_input)
        layout.addWidget(browse_button)
        box.setLayout(layout)

        return box

    def create_float_input_box(self, label_text):
        box = QGroupBox(label_text)
        box.setStyleSheet(self.get_dark_theme_style())
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 10, 20, 10)

        float_input = QDoubleSpinBox()
        float_input.setRange(-1e10, 1e10)
        float_input.setDecimals(5)
        float_input.setSingleStep(0.1)
        float_input.setFixedWidth(200)

        layout.addWidget(float_input, alignment=Qt.AlignmentFlag.AlignCenter)
        box.setLayout(layout)

        if label_text == "Start Time:":
            self.start_time = float_input
        elif label_text == "Stop Time:":
            self.stop_time = float_input

        return box

    def create_dropdown_menu(self):
        box = QGroupBox("Additional Options")
        box.setStyleSheet(self.get_dark_theme_style())
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 10, 20, 10)

        format_label = QLabel("Output Format:")
        self.format_dropdown = QComboBox()
        self.format_dropdown.addItems([".mat", ".csv"])
        self.format_dropdown.setFixedWidth(200)

        input_label = QLabel("Additional Input:")
        self.additional_input = QLineEdit()
        self.additional_input.setPlaceholderText("Optional input for OpenModelica")
        self.additional_input.setFixedWidth(400)

        layout.addWidget(format_label)
        layout.addWidget(self.format_dropdown, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(input_label)
        layout.addWidget(self.additional_input, alignment=Qt.AlignmentFlag.AlignLeft)
        box.setLayout(layout)

        return box

    def show_error_dialog(self, message: str) -> None:
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.exec()

    def select_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Select Executable", "", "Executable files (*.exe);;All files (*.*)"
        )
        if filename:
            self.file_input.setText(filename)

    def run_executable(self):
        exe_path = self.file_input.text()
        start_time = self.start_time.value()
        stop_time = self.stop_time.value()
        additional_input = self.additional_input.text()
        output_format = self.format_dropdown.currentText()

        try:
            if validate_inputs(exe_path, start_time, stop_time):
                run_simulation(exe_path, start_time, stop_time, additional_input, output_format)
        except ValidationError as e:
            self.show_error_dialog(str(e))

if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    # Set dark theme palette
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.ColorRole.Window, QColor("#1a1a1a"))
    dark_palette.setColor(QPalette.ColorRole.WindowText, QColor("#ffffff"))
    dark_palette.setColor(QPalette.ColorRole.Base, QColor("#2d2d2d"))
    dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#383838"))
    dark_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor("#ffffff"))
    dark_palette.setColor(QPalette.ColorRole.ToolTipText, QColor("#ffffff"))
    dark_palette.setColor(QPalette.ColorRole.Text, QColor("#ffffff"))
    dark_palette.setColor(QPalette.ColorRole.Button, QColor("#383838"))
    dark_palette.setColor(QPalette.ColorRole.ButtonText, QColor("#ffffff"))
    dark_palette.setColor(QPalette.ColorRole.Link, QColor("#0078d4"))
    dark_palette.setColor(QPalette.ColorRole.Highlight, QColor("#0078d4"))
    dark_palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#ffffff"))

    app.setPalette(dark_palette)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())