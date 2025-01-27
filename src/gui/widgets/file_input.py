from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QGroupBox,
    QFileDialog,
    QMessageBox,
)
from PyQt6.QtCore import Qt
from ..styles import get_dark_theme_style, get_button_style
import os


class FileInput(QWidget):
    """Widget for file selection with browse button."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """Initialize the UI components."""

        self.box = QGroupBox()
        self.box.setStyleSheet(get_dark_theme_style())

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Label
        label = QLabel("Select Executable")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 14px;
                margin-bottom: 5px;
            }
        """)

        # Input and button layout
        input_layout = QHBoxLayout()
        input_layout.setSpacing(10)

        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("Path to .exe file")
        self.file_input.setMinimumHeight(30)

        browse_button = QPushButton("Browse")
        browse_button.setStyleSheet(get_button_style())
        browse_button.setFixedWidth(100)
        browse_button.setMinimumHeight(30)
        browse_button.clicked.connect(self.select_file)

        input_layout.addWidget(self.file_input)
        input_layout.addWidget(browse_button)

        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(input_layout)
        self.box.setLayout(layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.box)
        self.setLayout(main_layout)

    def select_file(self):
        """Open file dialog for selecting executable."""
        user_home_directory = os.path.expanduser("~")
        username = os.path.basename(user_home_directory)
    
        
        specific_path = os.path.join(user_home_directory, "AppData", "Local", "Temp", "OpenModelica", "OMEdit", "NonInteractingTanks.TwoConnectedTanks")

        filename, _ = QFileDialog.getOpenFileName(
        self,
        "Select Executable",
        specific_path,  
        "Executable files (*.exe);;All files (*.*)"
    )
        if filename:
            self.file_input.setText(filename)

    def get_file_path(self) -> str:
        """Return the selected file path."""

        return self.file_input.text()

    def show_error_dialog(self, message: str):
        """Display error message dialog."""

        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Icon.Critical)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.exec()
