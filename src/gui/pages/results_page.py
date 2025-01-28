from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    QMessageBox
)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
import os
from pathlib import Path

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
        self._add_description_label(layout)
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

    def _add_description_label(self, layout):
        desc_label = QLabel("Your simulation results are ready to be downloaded...")
        desc_label.setStyleSheet(get_description_label_style())
        layout.addWidget(
            desc_label,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

    def _add_download_button(self, layout):
        download_button = QPushButton("Download Results")
        download_button.setStyleSheet(get_download_button_style())
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
        output_format = self.main_window.input_page.format_selector.get_selected_format()
        is_default = self.main_window.input_page.file_input.is_default()

        if is_default:
            self._save_to_default_location(output_format)
        else:
            self._save_with_dialog(output_format)

    def _save_to_default_location(self, output_format):
        try:
            current = Path(__file__).resolve()
            while current.name != 'src':
                current = current.parent
            current = current.parent

            filename = f"result{output_format}"
            save_path = os.path.join(current, filename)

            simulation_data = self.main_window.simulation_results

            if output_format == '.mat':
                from scipy.io import savemat
                savemat(save_path, {'simulation_data': simulation_data})
            else:
                import pandas as pd
                pd.DataFrame(simulation_data).to_csv(save_path, index=False)

            self.path_label.setText("")
        except Exception as e:
            self._show_error(str(e))

    def _save_with_dialog(self, output_format):
        default_name = "result" + output_format
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save Results",
            default_name,
            f"Results (*{output_format});;All Files (*)"
        )

        if filename:
            try:
                simulation_data = self.main_window.simulation_results

                if output_format == '.mat':
                    from scipy.io import savemat
                    savemat(filename, {'simulation_data': simulation_data})
                else:
                    import pandas as pd
                    pd.DataFrame(simulation_data).to_csv(filename, index=False)

                self.path_label.setText(f"This file is also saved in: {filename}")
            except Exception as e:
                self._show_error(str(e))

    def _show_error(self, message):
        QMessageBox.critical(self, "Error", message)