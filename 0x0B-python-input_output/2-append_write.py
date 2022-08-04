#!/usr/bin/python3
"""
4-append_write module
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, 'a') as af:
        return af.write(str(text))
