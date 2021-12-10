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
        self.maximize()

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
    
        self.source_selector = Gtk.FileChooserButton()
        self.source_selector.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        self.source_selector.connect("file-set", lambda a: threading.Timer(0.1, self.set_source_dir).start())

        hbox = Gtk.HBox()
        vbox = Gtk.VBox()
        hbox.pack_start(self.source_selector, False, False, 5)
        vbox.pack_start(hbox, True, True, 5)
        self.source_frame.add(vbox)
        self.dir_selector_box.pack_start(self.source_frame, True, True, 3)

        # The target directory selector
        self.target_frame = Gtk.Frame(label="Target")

        self.target_selector = Gtk.FileChooserButton()
        self.target_selector.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        self.target_selector.connect("file-set", lambda a: threading.Timer(0.1, self.set_source_dir).start())

        hbox = Gtk.HBox()
        vbox = Gtk.VBox()
        hbox.pack_start(self.target_selector, False, False, 5)
        vbox.pack_start(hbox, True, True, 5)
        self.target_frame.add(vbox)
        self.dir_selector_box.pack_start(self.target_frame, True, True, 3)

        self.dir_selector_box.show_all()

    def create_window(self):
        """Add all the widgets to the window."""

        # The main box
        self.main_box = Gtk.VBox()
        self.add(self.main_box)

        # Create the directory selectors
        self.create_dir_selectors()

    def set_source_dir(self):
        """Set the source directory variable."""
        self.source = self.source_selector.get_filename()

    def set_target_dir(self):
        """Set the target directory variable."""
        self.target = self.target_selector.get_filename()