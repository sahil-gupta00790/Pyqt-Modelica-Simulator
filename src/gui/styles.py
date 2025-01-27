from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QApplication


def get_dark_theme_style() -> str:
    """Return the dark theme stylesheet."""
    
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


def get_button_style() -> str:
    """Return the button stylesheet."""
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

