#!/usr/bin/python3
"""defines a class square"""


class Square:
    """represents the properties of a Square"""
    def __init__(mysquare, size):
        """initializes a new instance of a square

        Args:
            size: size of the square(one side)
        """
        mysquare.__size = size
