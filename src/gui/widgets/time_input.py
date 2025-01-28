from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGroupBox,
    QLineEdit
)
from PyQt6.QtCore import Qt
from ..styles import get_dark_theme_style
from PyQt6.QtGui import QDoubleValidator


class TimeInput(QWidget):
    """Widget for time input with spinbox."""

    def __init__(self, label_text: str, parent=None):
        super().__init__(parent)
        self.label_text = label_text
        self.setup_ui()

    def setup_ui(self):
        """Initialize the UI components."""
        box = QGroupBox()
        box.setStyleSheet(get_dark_theme_style())

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label = QLabel(self.label_text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.time_input = QLineEdit()
        validator = QDoubleValidator(0, 5, 6)
        
        self.time_input.setValidator(validator)

        self.time_input.setFixedWidth(200)
        self.time_input.setMinimumHeight(30)
        self.time_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        
        self.time_input.setText("0.00")
        self.time_input.editingFinished.connect(self._clean_trailing_zeros)
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.time_input, alignment=Qt.AlignmentFlag.AlignCenter)
        box.setLayout(layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(box)
        self.setLayout(main_layout)
    def _clean_trailing_zeros(self):
        """Clean up trailing zeros while keeping at least 2 decimal places"""
        try:
            value = float(self.time_input.text())
            text = f"{value:.6f}".rstrip('0')
            if '.' in text:
                decimal_places = len(text.split('.')[1])
                if decimal_places < 2:
                    text = f"{value:.2f}"
            self.time_input.setText(text)
        except ValueError:
            pass

    def get_value(self) -> float:
        """Return the current time value."""
        try:
            return float(self.time_input.text())
        except ValueError:
            return 0.0

    