#!/usr/bin/python3
"""defines a class square"""


class Square:
    """represents the properties of a Square"""

    def __init__(mysquare, size=0):
        """initilizes a new instance of square
        args:
            size(int): size of the square
        """
        mysquare.__size = size

    @property
    def size(mysquare):
        """get the current size of sqaure"""
        return mysquare.__size

    @size.setter
    def size(mysquare, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        mysquare.__size = value

    def area(mysquare):
        """return the area of the square"""
        return (mysquare.__size ** 2)
