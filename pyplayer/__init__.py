# Project: PyPlayer
# Authored by:
#  - Nelson Crosby (github.com/NelsonCrosby)
#  - Riley Steyn (github.com/RSteyn)

from pyplayer import windows
from pyplayer import functions as fns


def prepare():
    """Parse arguments; ensure the system is prepared"""
    pass


def run():
    """Initiate the GUI"""
    gui = windows.MainWindow()
    gui.mainloop()
