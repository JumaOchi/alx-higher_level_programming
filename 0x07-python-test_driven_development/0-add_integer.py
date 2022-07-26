#!/us/bin/python3
"""Function that adds 2 integers"""


def add_integer(a, b=98):
"""defining function variables"""

if (isinstance(a, int) or isinstance(a, float) and\
        (isinstance(b, int) or isinstance(b, float)):
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)
        return a + b
        elif not (isinstance(a, int) or isinstance(a, float)):
            raise TypeError("a must be an integer")
        elif not (isinstance(b, int) or isinstance(b, float)):
            raise TypeError("b must be an integer")
