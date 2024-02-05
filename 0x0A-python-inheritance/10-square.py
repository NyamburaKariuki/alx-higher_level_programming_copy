#!/usr/bin/python3
"""module that inherits from Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from the class Rectangle"""
    
    def __init__(self, size)
        self.integer_validator("size", size)
        self.__size = size
