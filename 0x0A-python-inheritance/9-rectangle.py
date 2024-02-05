#!/usr/bin/python3
"""module inherits from Geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry Class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """claculates the area of a triangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints the description of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
