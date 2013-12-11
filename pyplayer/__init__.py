# Project: PyPlayer
# Authored by:
#  - Nelson Crosby (github.com/NelsonCrosby)
#  - Riley Steyn (github.com/RSteyn)

import sys


# Ensure the correct packages are importable.
try:
    # noinspection PyUnresolvedReferences
    import tkinter
except ImportError:
    print("Cannot import tkinter\n"
          "Please ensure that tkinter is installed (see README.md).\n"
          "Failing that, I (github.com/NelsonCrosby) would be very\n"
          "interested in hearing about your issue.", file=sys.stderr)
    print("Execution failed, exiting (1)", file=sys.stderr)
    sys.exit(1)
# tkinter does not need to remain in this namespace.
del tkinter

from pyplayer import windows
from pyplayer import functions
fns = functions


def run():
    """Initiate the GUI"""
    gui = windows.MainWindow()
    gui.mainloop()
