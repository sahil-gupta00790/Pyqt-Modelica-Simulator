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
    QCheckBox {
        color: #ffffff;
        font-size: 12px;
        margin-top: 5px;
    }
    QCheckBox::indicator {
        width: 15px;
        height: 15px;
        border-radius: 3px;
    }
    QCheckBox::indicator:unchecked {
        background-color: #383838;
        border: 1px solid #3d3d3d;
    }
    QCheckBox::indicator:unchecked:hover {
        border: 1px solid #0078d4;
    }
    QCheckBox::indicator:checked {
        background-color: #0078d4;
        border: 1px solid #0078d4;
    }
    QCheckBox::indicator:checked:hover {
        background-color: #1484d7;
        border: 1px solid #1484d7;
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


def get_download_button_style() -> str:
    """Return the download button stylesheet."""
    return """
    QPushButton {
        background-color: #2ecc71;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 14px;
        min-width: 120px;
        max-width: 200px;
    }
    QPushButton:hover {
        background-color: #27ae60;
    }
    QPushButton:pressed {
        background-color: #219a52;
    }
    """


def get_description_label_style() -> str:
    """Return the description label stylesheet."""
    return """
    color: #a0a0a0;
    font-family: 'Segoe Script', cursive;
    font-size: 16px;
    margin: 20px;
    """


def get_results_label_style() -> str:
    """Return the results label stylesheet."""
    return "color: white; font-size: 24px;"


def get_path_label_style() -> str:
    """Return the path label stylesheet."""
    return "color: #a0a0a0; font-size: 12px;"

def get_back_button_style() -> str:
    """Return the back button stylesheet."""
    return """
    QPushButton {
        background-color: #2d2d2d;
        
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 14px;
        text-align: left;
        min-width: 120px;
    }
    QPushButton:hover {
        color: #ffffff;
        background-color: #353535;
    }
    QPushButton:pressed {
        background-color: #404040;
    }
    """