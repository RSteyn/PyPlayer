# Project: PyPlayer
# Authored by:
#  - Nelson Crosby (github.com/NelsonCrosby)
#  - Riley Steyn (github.com/RSteyn)

import sys


class Functions:

    def __init__(self):
        self.to_clean = []

    def register_method_to_clean(self, clean_function):
        """

        @type clean_function: function
        """
        self.to_clean.append(clean_function)

    def deregister_method_to_clean(self, clean_function):
        """

        @type clean_function: function
        """
        self.to_clean.remove(clean_function)

    def done(self):
        """Quit the application in a stable way.
        This may involve more as development progresses."""

        for function in self.to_clean:
            function()

        sys.exit(0)

# THIS IS VALID I'VE SEEN IT IN random.py
_inst = Functions()
register_method_to_clean = _inst.register_method_to_clean
deregister_method_to_clean = _inst.deregister_method_to_clean
done = _inst.done
