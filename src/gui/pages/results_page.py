from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    QMessageBox,
    
)
from PyQt6.QtGui import QPalette, QColor,QIcon
from PyQt6.QtCore import Qt,QSize
import os
from pathlib import Path
from ..widgets.format_selector import FormatSelector
from ..widgets.file_input import FileInput
import shutil

from ..styles import (
    get_button_style,
    get_download_button_style,
    get_description_label_style,
    get_results_label_style,
    get_path_label_style
)


class ResultsPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setup_ui()

    def setup_ui(self):
        self._setup_palette()
        layout = QVBoxLayout()
        self._add_results_label(layout)
        self._add_description_label(layout,"Bruh")
        self._add_download_button(layout)
        self._add_path_label(layout)
        self._add_back_button(layout)
        layout.addStretch()
        self.setLayout(layout)

    def _setup_palette(self):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#1a1a1a"))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

    def _add_results_label(self, layout):
        results_label = QLabel("Simulation Results")
        results_label.setStyleSheet(get_results_label_style())
        layout.addWidget(
            results_label,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

    def _add_description_label(self, layout,str):
        desc_label = QLabel(str)
        desc_label.setStyleSheet(get_description_label_style())
        layout.addWidget(
            desc_label,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

    def _add_download_button(self, layout):
        download_button = QPushButton("Download Results")
        download_button.setStyleSheet(get_download_button_style())
        download_icon = QIcon("image.png")
        download_button.setIconSize(QSize(24, 24))
        download_button.setIcon(download_icon)
        download_button.clicked.connect(self.download_results)
        layout.addWidget(
            download_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

    def _add_path_label(self, layout):
        self.path_label = QLabel("")
        self.path_label.setStyleSheet(get_path_label_style())
        self.path_label.setWordWrap(True)
        layout.addWidget(
            self.path_label,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

    def _add_back_button(self, layout):
        back_button = QPushButton("Back to Input")
        back_button.setStyleSheet(get_button_style())
        back_button.clicked.connect(self.main_window.go_to_input_page)
        layout.addWidget(
            back_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

    def download_results(self):
        output_format = self.main_window.selected_format
        is_default = self.main_window.is_default

        if is_default:
            self._save_to_default_location(output_format)
        else:
            self._save_with_dialog(output_format)

    def _save_to_default_location(self, output_format):
        current = Path(__file__).resolve()
        while current.name != 'src':
            current = current.parent
        current=current.parent
        path=os.path.join(current,'model','executables')
        if output_format== '.mat':
            options = QFileDialog.Option.DontUseNativeDialog 
            file_path,_=QFileDialog.getSaveFileName(
                self,
                "Save file as",
                "Result.mat",
                "MATLAB Files (*.mat)",
                options=options
            )
            if file_path:
                try:
                    shutil.copy(os.path.join(path,"result.mat"),file_path)
                    QMessageBox.information(self,"Success","File saved successfully")
                except Exception as e:
                    self._show_error(f"Failed to save file {e}")
        else:
            options = QFileDialog.Option.DontUseNativeDialog 
            file_path,_=QFileDialog.getSaveFileName(
                self,
                "Save file as",
                "Result.csv",
                "CSV Files(*.csv)",
                options=options
            )
        if file_path:
            try:
                shutil.copy(os.path.join(path,"result.csv"),file_path)
                QMessageBox.information(self,"Success","File saved successfully")
            except Exception as e:
                self._show_error(f"Failed to save file {e}")


    def _save_with_dialog(self, output_format):
        exe_dir = os.path.dirname(self.main_window.path)
        if output_format== '.mat':
            options = QFileDialog.Option.DontUseNativeDialog 
            file_path,_=QFileDialog.getSaveFileName(
                self,
                "Save file as",
                "Result.mat",
                "MATLAB Files (*.mat)",
                options=options
            )
            if file_path:
                try:
                    shutil.copy(os.path.join(exe_dir,"result.mat"),file_path)
                    QMessageBox.information(self,"Success","File saved successfully")
                except Exception as e:
                    self._show_error(f"Failed to save file {e}")
        else:
            options = QFileDialog.Option.DontUseNativeDialog 
            file_path,_=QFileDialog.getSaveFileName(
                self,
                "Save file as",
                "Result.csv",
                "CSV Files(*.csv)",
                options=options
            )
            if file_path:
                try:
                    shutil.copy(os.path.join(exe_dir,"result.csv"),file_path)
                    QMessageBox.information(self,"Success","File saved successfully")
                except Exception as e:
                    self._show_error(f"Failed to save file {e}")



    def _show_error(self, message):
        QMessageBox.critical(self, "Error", message)