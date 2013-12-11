PyPlayer
========

A very basic media player project. Because why the hell not.


Running
=======

Assuming that Python is in your PATH and default is Python 3:

$ python main.py

Will run the program.

Requirements
============

This application is designed for CPython 3.2 - 3.3 (sorry Mac users, we know
this is a pain in the butt).

You will have to ensure that TkInter is installed. It should have come with Python.
If you installed from the binaries on python.org, then you don't have to worry.

Python installed via apt on Ubuntu (and possibly other Linux distro equivalents)
does not have TkInter installed by default. You may have to do something like:

$ sudo apt-get install python3-tk

or distro equivalent. Other distros may have to use a package browser to find
the correct package.

The audio library is currently undecided. Rest assured, we will ensure that
it claims to be compatible with all major OS's, and we will include the
source so the application can self-install.
