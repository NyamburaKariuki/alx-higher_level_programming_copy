#!/usr/bin/python3
"""module contain the base class, its attributes and methods"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1,1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy
