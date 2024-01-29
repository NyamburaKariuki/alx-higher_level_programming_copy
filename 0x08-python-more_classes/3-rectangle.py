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
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """gets the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the new height of  the rectangle"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        """returns the area rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints the rectangle with the character #"""

        if self.__width == 0 or self.__height == 0:
            return ""
        result = []
        for h in range(self.__height):
            [result.append('#') for w in range(self.__width)]
            if h != self.__height - 1:
                result.append("\n")
        return ("".join(result))

