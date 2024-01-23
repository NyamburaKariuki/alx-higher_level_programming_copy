#!/usr/bin/python3
"""represents the properties of a Square"""


class Square:
    """represents the properties of a Square"""

    def __init__(self, size=0):
        """initilizes a new instance of square
        args:
             size(int): size of the square"""
        self.__size = size

    @property
    def size(self):
        """get the current size of sqaure"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        for x in range(self.__size):
            print("#" * self.__size)
