"""The main application."""

import PyQt5 as qt
from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QAction, QApplication, QGridLayout

class Window(QWindow):
    """The main application window."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.show()