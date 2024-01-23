#!/usr/bin/python3
"""defines a class square"""


class Square:
    """represents the properties of a Square"""

    def __init__(mysquare, size=0):
        """initializes a new instance of square
        args:
            Size(int): size of the square, one side
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        mysquare.__size = size

    def area(mysquare):
        """returns the current square area"""
        return (mysquare.__size **2)
