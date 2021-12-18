"""The Sortery App is a simple gui that uses the Sortery command-line file sorter."""

import app
import sys

# Run the app
application = app.QApplication([])
application.setApplicationName("Sortery App")
window = app.Window()
application.exec_()