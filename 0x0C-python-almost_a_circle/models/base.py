#!/usr/bin/python3
'''
program to manage id in this project
'''

class Base:
"""
Define the Base class
"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize variables and methods"""
        if id is not None:
            self.id = id
        else:
             Base.__nb_objects += 1
             self.id = Base.__nb_objects
