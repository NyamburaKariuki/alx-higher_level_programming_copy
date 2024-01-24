#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """class that defines property of a square"""

    def __init__(self, size=0):
        """initializes an ainstance of class square
        args:
            size(int)"""
        self.size = size

    @property
    def size(self):
        """returns the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of  ac circle"""
        return self.__size ** 2

    def __eq__(self, other):
        """checks if square area is equal to another
        retuns true or False
        args:
            other(area of another square)"""
        return self.area() == other.area()

    def __ne__(self, other):
        """checks if square area is not equal to the other
        returns true or false
        args: other(area of another square)"""
        return self.area() != other.area()

    def __gt__(self, other):
        """checks if sq area is greater than the other
        returns True or False
        args:other(another square)"""
        return self.area() > other.area()

    def __ge__(self, other):
        """checks if sq area is greater or equal to another
        returns True or False
        args:other(another square)"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """check if the sq area is less than another
        returns True or False
        args:other(another square)"""
        return self.area() < other.area()

    def __le__(self, other):
        """checks if the sq area is less or equal to another
        returns True or False
        args: other(another square)"""
        return self.area() <= other.area()
