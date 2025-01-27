from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QGroupBox,
    QComboBox,
)
from PyQt6.QtCore import Qt
from ..styles import get_dark_theme_style


class FormatSelector(QWidget):
    """Widget for selecting output format."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """Initialize the UI components."""

        container = QWidget()
        layout = QVBoxLayout(container)

        self.options_label = QPushButton("Additional Option \u25B6")
        self.options_label.setStyleSheet("""
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
        self.options_label.setCursor(Qt.CursorShape.PointingHandCursor)
        self.options_label.clicked.connect(self.toggle_format_box)

        self.format_dropdown = QComboBox()
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
                min-width: 460px;
            }
        """)

        # Create group box for format selection
        self.format_box = QGroupBox()
        self.format_box.setStyleSheet(get_dark_theme_style())

        box_layout = QVBoxLayout()
        box_layout.setContentsMargins(20, 15, 20, 15)
        box_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label = QLabel("Select Output Format")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        box_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        box_layout.addWidget(
            self.format_dropdown,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.format_box.setLayout(box_layout)
        self.format_box.setVisible(False)

        layout.addWidget(
            self.options_label,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        layout.addWidget(self.format_box, alignment=Qt.AlignmentFlag.AlignLeft)

        main_layout = QVBoxLayout()
        main_layout.addWidget(container)
        self.setLayout(main_layout)

    def toggle_format_box(self):
        """Toggle the visibility of the format selection box."""

        is_visible = self.format_box.isVisible()
        self.format_box.setVisible(not is_visible)
        
        # Update arrow direction
        arrow = "\u25BC" if not is_visible else "\u25B6"
        self.options_label.setText(f"Additional Option {arrow}")

    def get_selected_format(self) -> str:
        """Return the selected format."""

        return self.format_dropdown.currentText()