"""The main application."""

import gi
import threading

gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gtk

class App(Gtk.Application):
    """The Sortery App."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="sortery.app", **kwargs)

        # The one window
        self.window = None

    def do_activate(self):
        """Activate the app."""

        # Create the window, if it doesn't already exist
        if self.window is None:
            self.window = AppWindow(application=self)
            self.window.present()

    def do_starup(self):
        """Startup the application."""
        Gtk.Application.startup(self)

class AppWindow(Gtk.ApplicationWindow):
    """The window for the Sortery application."""

    def __init__(self, *args, application, **kwargs):
        super().__init__(*args, application=application, title="Sortery App", **kwargs)

        # Create the window and all its widgets
        self.create_window()

        # The source and target directories
        self.source = ""
        self.target = ""

        self.show_all()

    def create_dir_selectors(self):
        """Create the directory selectors."""

        # The dir selector box
        self.dir_selector_box = Gtk.HBox()
        self.main_box.pack_start(self.dir_selector_box, False, True, 3)

        # The source directory selector
        self.source_frame = Gtk.Frame(label="Source")
        self.source_box = PaddedBox(False)
        self.source_frame.add(self.source_box)
    
        self.source_selector = Gtk.FileChooserButton()
        self.source_selector.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        self.source_selector.connect("file-set", lambda a: threading.Timer(0.1, self.set_source_dir).start())
        self.source_box.pack_start_auto_pad(self.source_selector, False, True)

        self.dir_selector_box.pack_start(self.source_frame, True, True, 3)

        # The target directory selector
        self.target_frame = Gtk.Frame(label="Target")
        self.target_box = PaddedBox(False)
        self.target_frame.add(self.target_box)

        self.target_selector = Gtk.FileChooserButton()
        self.target_selector.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        self.target_selector.connect("file-set", lambda a: threading.Timer(0.1, self.set_source_dir).start())
        self.target_box.pack_start_auto_pad(self.target_selector, False, True)

        self.dir_selector_box.pack_start(self.target_frame, True, True, 3)

        self.dir_selector_box.show_all()

    def create_option_widgets(self):
        """Create the checkbuttons to configure the options."""

        # The options containers
        self.options_base_box = Gtk.HBox()
        self.options_frame = Gtk.Frame(label="Options")
        self.options_base_box.pack_start(self.options_frame, True, True, 3)
        self.main_box.pack_start(self.options_base_box, True, True, 3)

        self.options_box = PaddedBox(False)
        self.options_frame.add(self.options_box)

        self.date_format_box = PaddedBox(False, False)

        # The preserve-name checkbutton
        self.preserve_name_checkbutton = Gtk.CheckButton(label="Preserve Name")
        self.options_box.pack_start_auto_pad(self.preserve_name_checkbutton, True, True)

        # The date-format checkbutton and entry
        self.date_format_checkbutton = Gtk.CheckButton(label="Date Format")
        self.date_format_box.pack_start_auto_pad(self.date_format_checkbutton, True, True)
        
        self.date_format_entry = Gtk.Entry()
        self.date_format_entry.set_placeholder_text("Date Format")
        self.date_format_box.pack_end_auto_pad(self.date_format_entry, True, True)

        self.options_box.pack_end_auto_pad(self.date_format_box, True, True)

        # The date-format settings
        self.date_format_frame = Gtk.Frame(label="Date Format")
        self.date_format_box = PaddedBox(False)
        self.date_format_frame.add(self.date_format_box)
        self.options_box.pack_start_auto_pad(self.date_format_frame, True, True)

        self.created_radio_button = Gtk.RadioButton(label="Created")
        self.date_format_box.pack_start_auto_pad(self.created_radio_button, True, True)
        
        self.modified_radio_button = Gtk.RadioButton.new_from_widget(self.created_radio_button)
        self.modified_radio_button.set_label("Modified")
        self.date_format_box.pack_start_auto_pad(self.modified_radio_button, True, True)
        
        self.accessed_radio_button = Gtk.RadioButton.new_from_widget(self.created_radio_button)
        self.accessed_radio_button.set_label("Accessed")
        self.date_format_box.pack_start_auto_pad(self.accessed_radio_button, True, True)

        

    def create_window(self):
        """Add all the widgets to the window."""

        # The main box
        self.main_box = Gtk.VBox()
        self.add(self.main_box)

        # Create the directory selectors
        self.create_dir_selectors()

        # Create the option-setting widgets
        self.create_option_widgets()

    def set_source_dir(self):
        """Set the source directory variable."""
        self.source = self.source_selector.get_filename()

    def set_target_dir(self):
        """Set the target directory variable."""
        self.target = self.target_selector.get_filename()

class PaddedBox(Gtk.VBox):
    """A custom box that supports padding both ways."""

    def __init__(self, expand=True, fill=True, padding=3):
        super().__init__()
        self.padding = padding

        # Our hbox
        self.hbox = Gtk.HBox()
        self.pack_start(self.hbox, expand, fill, self.padding)

        self.show_all()

    def pack_end_auto_pad(self, child, expand, fill):
        """Pack CHILD into self.hbox according to EXPAND and FILL, both bools."""
        self.hbox.pack_end(child, expand, fill, self.padding)
        self.hbox.show_all()

    def pack_start_auto_pad(self, child, expand, fill):
        """Pack CHILD into self.hbox according to EXPAND and FILL, both bools."""
        self.hbox.pack_start(child, expand, fill, self.padding)
        self.hbox.show_all()