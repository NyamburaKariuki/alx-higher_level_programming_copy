#!/usr/bin/python3
"""module contain the base class, its attributes and methods"""


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """instancitaion of a class'''
        args: Id(integer)"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
