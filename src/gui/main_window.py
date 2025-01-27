from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                           QPushButton, QFileDialog, QLineEdit, QLabel,
                           QMessageBox, QGroupBox, QDoubleSpinBox, QComboBox)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
from utils.validator import validate_inputs, ValidationError
from utils.simulator import run_simulation
from PyQt6.QtWidgets import QToolButton, QMenu

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
        QDoubleSpinBox {
        background-color: #383838;
        color: #ffffff;
        border: 1px solid #3d3d3d;
        border-radius: 4px;
        padding: 5px;
        min-height: 30px;
    }
        QLabel {
            color: #ffffff;
        }
        QLineEdit, QComboBox {
            background-color: #383838;
            border: 1px solid #3d3d3d;
            border-radius: 4px;
            padding: 5px;
            color: #ffffff;
        }
        QLineEdit:focus, QDoubleSpinBox:focus, QComboBox:focus {
            border: 1px solid #0078d4;
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
        self.start_time_box = self.create_float_input_box("Start Time")
        self.stop_time_box = self.create_float_input_box("Stop Time")
        content_layout.addWidget(self.start_time_box)
        content_layout.addWidget(self.stop_time_box)

        # Dropdown menu with additional options
        self.dropdown_menu = self.create_dropdown_menu()
        content_layout.addWidget(self.dropdown_menu)
        

        # Execute button
        self.execute_button = QPushButton("Execute Simulation")
        
        self.execute_button.setStyleSheet(self.get_button_style())
        self.execute_button.clicked.connect(self.run_executable)
        content_layout.addWidget(self.execute_button,alignment=Qt.AlignmentFlag.AlignCenter)


        # Add container to main layout with alignment
        layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)
        central_widget.setLayout(layout)

    def create_file_explorer_box(self):
        box = QGroupBox()  # Remove the title as we'll add a centered label
        box.setStyleSheet(self.get_dark_theme_style())

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add centered label
        label = QLabel("Select Executable")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 14px;
                margin-bottom: 5px;
            }
        """)

        # Create horizontal layout for input and button
        input_layout = QHBoxLayout()
        input_layout.setSpacing(10)  # Space between input and button

        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("Path to .exe file")
        self.file_input.setMinimumHeight(30)  # Match the height of time inputs

        browse_button = QPushButton("Browse")
        browse_button.setStyleSheet(self.get_button_style())
        browse_button.setFixedWidth(100)
        browse_button.setMinimumHeight(30)  # Match the height
        browse_button.clicked.connect(self.select_file)

        input_layout.addWidget(self.file_input)
        input_layout.addWidget(browse_button)

        # Add widgets to main layout
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(input_layout)
        box.setLayout(layout)

        return box

    def create_float_input_box(self, label_text):
        box = QGroupBox()
        box.setStyleSheet(self.get_dark_theme_style())

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label = QLabel(label_text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        float_input = QDoubleSpinBox()
        float_input.setRange(0,5)
        float_input.setDecimals(2)
        float_input.setSingleStep(0.1)
        float_input.setFixedWidth(200)
        float_input.setMinimumHeight(30)
        float_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        float_input.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)

        



        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(float_input, alignment=Qt.AlignmentFlag.AlignCenter)
        box.setLayout(layout)

        if label_text == "Start Time":
            self.start_time_input = float_input
        elif label_text == "Stop Time":
            self.stop_time_input = float_input

        return box
    
    def create_dropdown_menu(self):
        container = QWidget()
        layout = QVBoxLayout(container)

        # Additional Options label
        self.additional_options_label = QPushButton("Additional Option \u25B6")
        self.additional_options_label.setStyleSheet("""
            QPushButton {
                background: none;
                border: none;
                color: #ffffff;
                font-size: 14px;
                text-align: left;
            }
            QPushButton:hover {
                color: #0078d4;
            }
        """)
        self.additional_options_label.setCursor(Qt.CursorShape.PointingHandCursor)
        self.additional_options_label.clicked.connect(self.toggle_output_format_box)

        # Create dropdown
        self.format_dropdown = QComboBox()  # Changed from output_format_dropdown to format_dropdown
        self.format_dropdown.addItem(".mat")
        self.format_dropdown.addItem(".csv")
        self.format_dropdown.setFixedWidth(200)
        self.format_dropdown.setMinimumHeight(30)
        self.format_dropdown.setStyleSheet("""
            QComboBox {
                background-color: #383838;
                color: #ffffff;
                border: 1px solid #3d3d3d;
                border-radius: 4px;
                padding: 5px;
                min-height: 30px;
                min-width: 500px;
                max-width: 500px;
            }
            QComboBox:drop-down {
                border: none;
                padding-right: 20px;
            }
            QComboBox:down-arrow {
                image: none;
            }
            QComboBox QAbstractItemView {
                background-color: #383838;
                color: #ffffff;
                selection-background-color: #0078d4;
                border: 1px solid #3d3d3d;
            }
        """)

        # Create label
        label = QLabel("Select Output Format")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create group box
        box = QGroupBox()
        box.setStyleSheet(self.get_dark_theme_style())

        # Layout for dropdown box
        dropdown_layout = QVBoxLayout()
        dropdown_layout.setContentsMargins(20, 15, 20, 15)
        dropdown_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add widgets to layouts
        dropdown_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        dropdown_layout.addWidget(self.format_dropdown, alignment=Qt.AlignmentFlag.AlignCenter)

        box.setLayout(dropdown_layout)
        box.setVisible(False)

        layout.addWidget(self.additional_options_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(box, alignment=Qt.AlignmentFlag.AlignLeft)

        self.output_format_box = box
        return container

    def toggle_output_format_box(self):
        # Toggle visibility of the entire output format box
        is_visible = self.output_format_box.isVisible()
        self.output_format_box.setVisible(not is_visible)

        # Update the label's arrow direction
        if is_visible:
            self.additional_options_label.setText("Additional Option \u25B6")  # Right arrow
        else:
            self.additional_options_label.setText("Additional Option \u25BC")  # Down arrow

    def show_error_dialog(self, message: str) -> None:
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Icon.Critical)
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
        start_time = self.start_time_input.value()
        stop_time = self.stop_time_input.value()
        output_format = self.format_dropdown.currentText()  # This now matches the widget name

        try:
            if validate_inputs(exe_path, start_time, stop_time):
                run_simulation(exe_path, start_time, stop_time, output_format)
        except ValidationError as e:
            self.show_error_dialog(str(e))
        except FileNotFoundError as e:
            self.show_error_dialog(str(e))
        except Exception as e:
            self.show_error_dialog("Simulation error. Please try again.")

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