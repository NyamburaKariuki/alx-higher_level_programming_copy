#!/usr/bin/python3
"""defines a class rectangle"""


class Rectangle:
    """represents the properties of a Square"""

    def __init__(self, width=0, height=0):
        """initializes a new instance of a square
        Args:
            width: base of the rectangle(int/float)
            height: height of the rectangle(int/floar)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle and assign it a value"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """gets the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the new height of  the rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
