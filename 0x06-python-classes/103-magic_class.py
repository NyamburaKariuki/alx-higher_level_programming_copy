#!/usr/bin/python3
"""Define a magic class that does the same as the provided python bytecode"""


import math


class MagicClass:
    """creates a class"""

    def __init__(self, radius=0):
        """initializes a class
        args: radius(float/int)
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """return the area of the MagicClass"""
        return self.__radius ** 2 * math.pi

    def circumfrence(self):
        """Returns the circumfrence of the Magic class"""
        return 2 * math.pi * self.__radius
