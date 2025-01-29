import os

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ..styles import (
    get_back_button_style,
    get_dark_theme_style,
    get_download_button_style,
)
from utils.file_operations import FileOperations


class ResultsPage(QWidget):
    """Results page widget that displays simulation results and download functionality."""
    
    def __init__(self, main_window):
        """Initialize the results page.
        
        Args:
            main_window: Parent window containing this widget.
        """
        super().__init__()
        self.main_window = main_window
        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface components and layouts for the results page.
        
        Creates a centered layout with a group box containing:
        - Results title
        - Download button
        - Status label
        - Back button
        """
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(20, 20, 20, 20)

        self.box = QGroupBox()
        self.box.setStyleSheet(get_dark_theme_style())
        self.box.setMinimumWidth(500)
        self.box.setFixedWidth(500)
        self.box.setMaximumHeight(300)

        box_layout = QVBoxLayout()
        box_layout.setContentsMargins(20, 15, 20, 15)
        box_layout.setSpacing(10)

        results_label = QLabel("Simulation Results")
        results_label.setStyleSheet(
            "color: white; font-size: 24px; font-weight: bold;"
        )
        box_layout.addWidget(
            results_label, 
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        
        
        download_button = QPushButton("Download Results")
        download_button.setStyleSheet(get_download_button_style())
        download_button.clicked.connect(self.download_results)
        download_button.setMinimumHeight(30)
        box_layout.addWidget(
            download_button, 
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.status_label = QLabel("")
        self.status_label.setStyleSheet(
            "color: #ffffff; "
            "font-size: 14px; "
            "font-family: 'Consolas', 'Courier New', monospace; "
            "margin-top: 10px; "
            "margin-bottom: 10px;"
        )
        self.status_label.setWordWrap(True)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        box_layout.addWidget(self.status_label)

        box_layout.addStretch(1)

        back_layout = QHBoxLayout()
        back_layout.setContentsMargins(0, 0, 0, 0)
        
        back_button = QPushButton("← Back")
        back_button.setStyleSheet(get_back_button_style())
        back_button.clicked.connect(self.main_window.go_to_input_page)
        back_button.setMinimumHeight(30)
        back_button.setMinimumWidth(120)
        
        back_layout.addWidget(back_button)
        back_layout.addStretch(1)
        box_layout.addLayout(back_layout)

        self.box.setLayout(box_layout)
        main_layout.addWidget(self.box)
        self.setLayout(main_layout)

    def set_status_text(self, text: str) -> None:
        """Update the status label text.
        
        Args:
            text: The new text to display in the status label.
        """
        self.status_label.setText(text)

    def download_results(self) -> None:
        """Handle the download results action.
        
        Determines the appropriate file path based on whether using default or 
        custom location, then triggers the file save operation through 
        FileOperations utility.
        """
        output_format = self.main_window.selected_format
        is_default = self.main_window.is_default
        is_mat = output_format == '.mat'

        if is_default:
            save_path = FileOperations.get_default_save_path()
            filename = "result.mat" if is_mat else "result.csv"
            source_path = os.path.join(save_path, filename)
        else:
            exe_dir = os.path.dirname(self.main_window.path)
            
            filename = "result.mat" if is_mat else "result.csv"
            source_path = os.path.join(exe_dir, filename)

        FileOperations.save_result_file(self, source_path, is_mat)