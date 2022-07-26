#!/usr/bin/python3

"""Module prints a string with names"""

def say_my_name(first_name, last_name=""):
    """
    describing function say my name
    """

    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    else:
        return f"My name is {first_name} {last_name}"
