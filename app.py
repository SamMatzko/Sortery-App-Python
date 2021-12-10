"""The main application."""

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

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
        super().__init__(*args, application=application, **kwargs)

        self.show_all()