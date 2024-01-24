#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """represents the properties of a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """initilizes a new instance of square
        args: size(int)
            : position(tuple)"""
        self.size = size
        self.position = position

    def area(self):
        """return the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """get the current size of sqaure"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size
        args:
            value(int)"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """returns the cordinates of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__position[1]):
                print("")
            for y in range(self.__size):
                for z in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)
