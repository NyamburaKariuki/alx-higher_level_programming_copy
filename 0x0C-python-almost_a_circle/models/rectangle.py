#!/usr/bin/python3
"""Class rectangle inherits from base"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instance of a class rectangle
        attributes:
        width: width of the rectangle(int)
        height of the rectangle(int)
        id: id (int)"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an ineteger")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an ineteger")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of a triangle"""
        return self.__width * self.__height

    def display(self):
        """displays the triangle using '#' character"""
        for i in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """returns the string representation of a triangle"""
        return ("[Rectangle] ({}) {:d}/{:d} - {}/{}".format(
        self.id, self.__x, self.__y, self.__width, self.__height))
