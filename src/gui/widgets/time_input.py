from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGroupBox,
    QDoubleSpinBox,
)
from PyQt6.QtCore import Qt
from ..styles import get_dark_theme_style


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

        self.time_input = QDoubleSpinBox()
        self.time_input.setRange(0, 5)
        self.time_input.setDecimals(2)
        self.time_input.setSingleStep(0.1)
        self.time_input.setFixedWidth(200)
        self.time_input.setMinimumHeight(30)
        self.time_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_input.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)

        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.time_input, alignment=Qt.AlignmentFlag.AlignCenter)
        box.setLayout(layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(box)
        self.setLayout(main_layout)

    def get_value(self) -> float:
        """Return the current time value."""
        return self.time_input.value()