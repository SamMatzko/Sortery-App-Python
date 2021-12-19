"""The main application."""

import os
import PyQt5 as qt

from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    """The main application window."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Command-line running options
        self.source = ""
        self.target = ""

        # Create the window
        self.create_window()

        self.show()

    def check_startable(self):
        """Make the start button sensitive if both self.source and self.target
        are valid, and make it insensitive if they are not."""

        self.start_button.setEnabled(self.source != "" and self.target != "" and self.target != self.source)

    def choose_source(self):
        """Get the source directory from the user."""
        source = QFileDialog.getExistingDirectory(self, "Choose the source directory")

        # Set the button's text and tooltip
        if source != "":
            self.source = source
            if len(self.source) > 30:
                self.source_chooser.setText("&Source: ...%s" % self.source[-30:])
            else:
                self.source_chooser.setText("&Source: %s" % self.source)
        self.source_chooser.setToolTip(self.source)

        # Make the start button clickable if both source and target are specified
        self.check_startable()

    def choose_target(self):
        """Get the target directory from the user."""
        target = QFileDialog.getExistingDirectory(self, "Choose the target directory")

        # Set the button's text and tooltip
        if target != "":
            self.target = target
            if len(self.target) > 30:
                self.target_chooser.setText("&Target: ...%s" % self.target[-30:])
            else:
                self.target_chooser.setText("&Target: %s" % self.target)
        self.target_chooser.setToolTip(self.target)

        # Make the start button clickable if both source and target are specified
        self.check_startable()

    def create_command_line_options(self):
        """Create the checkbuttons and entries for the command-line options."""

        # The layout
        options_groupbox = QGroupBox("Options")
        self.options_layout = QGridLayout()
        options_groupbox.setLayout(self.options_layout)
        self.main_layout.addWidget(options_groupbox, 1, 0)

        # The preserve file name checkbox
        self.preserve_name_checkbox = QCheckBox("Preserve file name")
        self.preserve_name_checkbox.setToolTip("Preserve the original file name after the date")
        self.options_layout.addWidget(self.preserve_name_checkbox, 0, 0, 1, 2)

        # The date format chooser
        self.date_format_label = QLabel("Date Format:")
        self.date_format_label.setToolTip("The date format to rename the files with")
        self.date_format_chooser = QComboBox()
        self.date_format_chooser.setToolTip("The date format to rename the files with")
        self.date_format_chooser.setMinimumWidth(230)
        
        # The date format chooser's options
        self.date_format_chooser.addItem("yyyy-mm-dd HHhMMmSSs (2021-12-10 15h45m22s)", 0)
        self.date_format_chooser.addItem("No date", 1)

        self.date_format_label.setBuddy(self.date_format_chooser)
        self.options_layout.addWidget(self.date_format_label, 1, 0)
        self.options_layout.addWidget(self.date_format_chooser, 1, 1)

        # The date type radiobuttons
        radio_widget = QWidget()
        self.radiobutton_layout = QGridLayout()
        radio_widget.setLayout(self.radiobutton_layout)
        self.radiobutton_label = QLabel("Sort by date:")
        self.radiobutton_label.setToolTip("The date to sort all the files by.")
        self.radiobutton_label.setBuddy(radio_widget)
        self.options_layout.addWidget(self.radiobutton_label, 2, 0)
        self.options_layout.addWidget(radio_widget, 2, 1)
        
        self.created_radiobutton = QRadioButton("Created")
        self.radiobutton_layout.addWidget(self.created_radiobutton, 0, 0)
        self.modified_radiobutton = QRadioButton("Modified")
        self.radiobutton_layout.addWidget(self.modified_radiobutton, 1, 0)
        self.accessed_radiobutton = QRadioButton("Accessed")
        self.radiobutton_layout.addWidget(self.accessed_radiobutton, 2, 0)

        self.modified_radiobutton.setChecked(True)

        # The exclude type entry
        exclude_tooltip = (
            "File extensions (like .jpg, .mp4, etc.) to exclude from sorting.\n"
            'Separate each extension with a dash, for example: "jpg-mp4".'
        )
        self.exclude_type_label = QLabel("Exclude Type(s):")
        self.exclude_type_label.setToolTip(exclude_tooltip)
        self.exclude_type_entry = QLineEdit()
        self.exclude_type_entry.setToolTip(exclude_tooltip)
        self.exclude_type_label.setBuddy(self.exclude_type_entry)
        self.options_layout.addWidget(self.exclude_type_label, 3, 0)
        self.options_layout.addWidget(self.exclude_type_entry, 3, 1)

        # The only type entry
        only_tooltip = (
            "File extensions (like .jpg, .mp4, etc.) to excluively sort.\n"
            "All other files types will be ignored during sorting.\n"
            'Separate each extension with a dash, for example: "jpg-mp4".\n'
            'This option overrides the "exclude type" option.'
        )
        self.only_type_label = QLabel("Only Type(s):")
        self.only_type_label.setToolTip(only_tooltip)
        self.only_type_entry = QLineEdit()
        self.only_type_entry.setToolTip(only_tooltip)
        self.only_type_label.setBuddy(self.only_type_entry)
        self.options_layout.addWidget(self.only_type_label, 4, 0)
        self.options_layout.addWidget(self.only_type_entry, 4, 1)

    def create_dir_choosers(self):
        """Create the source and target directory choosers."""

        dir_groupbox = QGroupBox("Directories")
        self.dir_layout = QGridLayout()
        dir_groupbox.setLayout(self.dir_layout)
        self.main_layout.addWidget(dir_groupbox, 0, 0)
        
        # The source directory chooser
        self.source_chooser = QPushButton("Choose &Source...")
        self.source_chooser.setToolTip("The folder to get all the files from")
        self.source_chooser.clicked.connect(self.choose_source)
        self.dir_layout.addWidget(self.source_chooser, 0, 0)

        # The target directory chooser
        self.target_chooser = QPushButton("Choose &Target...")
        self.target_chooser.setToolTip("The folder to sort all the files into")
        self.target_chooser.clicked.connect(self.choose_target)
        self.dir_layout.addWidget(self.target_chooser, 0, 1)

    def create_window(self):
        """Add all the widgets to the window."""

        # The main layout
        self.main_layout = QGridLayout()
        layout = self.layout()
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(self.main_layout)

        # The source and target directory choosers
        self.create_dir_choosers()

        # The command-line options
        self.create_command_line_options()

        # The start button
        self.start_button = QPushButton("St&art")
        self.start_button.setEnabled(False)
        self.start_button.clicked.connect(self.start)
        self.main_layout.addWidget(self.start_button, 3, 0)

    def start(self):
        """Run the sorting algorithm with the user's custom options."""

        # Get the command-line options
        if self.created_radiobutton.isChecked():
            date_type = "c"
        elif self.accessed_radiobutton.isChecked():
            date_type = "a"
        else:
            date_type = "m"

        if self.preserve_name_checkbox.isChecked():
            preserve_name = "--preserve-name"
        else:
            preserve_name = ""

        if self.date_format_chooser.currentIndex() == 0:
            date_format = "%Y-%m-%d %Hh%Mm%Ss"
        elif self.date_format_chooser.currentIndex() == 1:
            date_format = ""

        exclude_type = ""
        only_type = ""
        if self.exclude_type_entry.text() != "":
            exclude_type = '--exclude-type="{}"'.format(self.exclude_type_entry.text().strip())
        if self.only_type_entry.text() != "":
            only_type = '--only-type="{}"'.format(self.only_type_entry.text().strip())

        # Run the command
        command = 'sortery "{}" "{}" sort {} --date-type="{}" --date-format="{}" {} {}'.format(
            self.source,
            self.target,
            preserve_name,
            date_type,
            date_format,
            exclude_type,
            only_type
        )
        os.system(command)