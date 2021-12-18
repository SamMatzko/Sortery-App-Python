"""The main application."""

import PyQt5 as qt
from PyQt5.QtGui import QWindow
# from PyQt5.QtWidgets import QAction, QApplication, QGridLayout, QGroupBox
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    """The main application window."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create the window
        self.create_window()

        self.show()

    def choose_source(self):
        """Get the source directory from the user."""
        print("Source...")

    def choose_target(self):
        """Get the target directory from the user."""
        print("Target...")

    def create_window(self):
        """Add all the widgets to the window."""

        # The main layout
        self.main_layout = QGridLayout()
        layout = self.layout()
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(self.main_layout)

        # The source and target directory choosers
        
        dir_groupbox = QGroupBox("Directories")
        self.dir_layout = QGridLayout()
        dir_groupbox.setLayout(self.dir_layout)
        self.main_layout.addWidget(dir_groupbox, 0, 0)
        
        # The source directory chooser
        self.source_chooser = QPushButton("Choose &Source...")
        self.source_chooser.clicked.connect(self.choose_source)
        self.dir_layout.addWidget(self.source_chooser, 0, 0)

        # The target directory chooser
        self.target_chooser = QPushButton("Choose &Target...")
        self.target_chooser.clicked.connect(self.choose_target)
        self.dir_layout.addWidget(self.target_chooser, 0, 1)