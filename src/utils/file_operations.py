import os
import shutil
from pathlib import Path
from typing import Tuple

from PyQt6.QtWidgets import QFileDialog, QMessageBox,QWidget


class FileOperations:
    """Utility class for file operations related to saving simulation results."""

    @staticmethod
    def get_default_save_path() -> str:
        """Get the default save path for results.
        
        Traverses up the directory tree until finding 'src' directory,
        then returns path to the executables folder.
        
        Returns:
            str: Path to the default save location for result files.
        """
        current = Path(__file__).resolve()
        while current.name != 'src':
            current = current.parent
        current = current.parent
        return os.path.join(current, 'model', 'executables')

    @staticmethod
    def save_result_file(
        parent_widget: QWidget,
        source_path: str,
        is_mat_file: bool = False
    ) -> bool:
        """Save the result file to user selected location.
        
        Args:
            parent_widget: Parent widget for the file dialog.
            source_path: Path to the source file to be copied.
            is_mat_file: If True, save as .mat file, otherwise as .csv.
        
        Returns:
            bool: True if file was saved successfully, False otherwise.
        
        Note:
            Uses non-native file dialog for consistent cross-platform behavior.
        """
        options = QFileDialog.Option.DontUseNativeDialog
        file_type = "MATLAB Files (*.mat)" if is_mat_file else "CSV Files (*.csv)"
        default_name = "Result.mat" if is_mat_file else "Result.csv"
        
        file_path, _ = QFileDialog.getSaveFileName(
            parent_widget,
            "Save file as",
            default_name,
            file_type,
            options=options
        )
        
        if not file_path:
            return False
            
        try:
            shutil.copy(source_path, file_path)
            QMessageBox.information(
                parent_widget,
                "Success",
                "File saved successfully"
            )
            return True
        except Exception as e:
            QMessageBox.critical(
                parent_widget,
                "Error",
                f"Failed to save file: {e}"
            )
            return False