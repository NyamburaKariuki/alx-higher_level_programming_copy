#!/usr/bin/python3
"""module contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class that inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialization of an instance
        args:
            size: size/width of the sqaure(int)
            x: the offset on the x axis(int)
            y: the offset on the y axis(int)
            id: identity of a new square"""

    super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0""")
        self.width = value
        self.height = value

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.__x, self.__y. self.__size))

    def update(self, *args, **kwargs):
        """updates the class with args and kwargs"""
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attribute[i], arg)
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)
