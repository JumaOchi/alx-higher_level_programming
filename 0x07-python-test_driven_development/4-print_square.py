#!/usr/bin/python3

"""
This module prints a square with character "#"
"""

def print_square(size):
    """defining function that prints a square"""

    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size >= 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end='')
            print("")
