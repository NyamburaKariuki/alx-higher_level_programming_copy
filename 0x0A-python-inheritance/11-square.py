#!/usr/bin/python3
"""module that inherits from Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from the class Rectangle"""

    def __init__(self, size):
        """creates an instance of class square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """prints the square representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """calculate the area of the square"""
        return self.__size * self.__size
