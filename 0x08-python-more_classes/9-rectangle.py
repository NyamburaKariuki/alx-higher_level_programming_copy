#!/usr/bin/python3
"""defines a class rectangle"""


class Rectangle:
    """represents the properties of a Square"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes a new instance of a square
        Args:
            width: base of the rectangle(int/float)
            height: height of the rectangle(int/floar)
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """gets the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle and assign it a value"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """gets the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the new height of  the rectangle"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        """returns the area rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size
        args: size(int)"""
        return (cls(size, size))

    def __str__(self):
        """prints the rectangle with the character #"""

        if self.__width == 0 or self.__height == 0:
            return ""
        res = []
        for h in range(self.__height):
            [res.append(str(self.print_symbol)) for w in range(self.__width)]
            if h != self.__height - 1:
                res.append("\n")
        return ("".join(res))

    def __repr__(self):
        """returns the string reperesentation of the rectabgle"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Print the message Bye rectangle...
        ... being 3 dots not ellipsis) when an instance of Rectangle is deleted
        """
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1
