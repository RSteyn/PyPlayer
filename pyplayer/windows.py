# Project: PyPlayer
# Authored by:
#  - Nelson Crosby (github.com/NelsonCrosby)
#  - Riley Steyn (github.com/RSteyn)

import tkinter as tk

from pyplayer import functions as fns


class MainWindow:
    """The main window for the application"""
    def __init__(self):
        self.root = tk.Tk()

        fns.register_method_to_clean(self.destroy)

        self._setup_widgets()

    def _setup_widgets(self):
        """Initiate the widgets in a separate method
        A bit nicer in terms of structure."""

    def mainloop(self):
        """Initiate the mainloop separately.
        This allows extra code to be executed before the window is shown, if necessary."""
        self.root.mainloop()

    def destroy(self):
        self.root.destroy()
        fns.deregister_method_to_clean(self.destroy)
