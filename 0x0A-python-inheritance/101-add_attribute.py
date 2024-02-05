#!/usr/bin/python3
"""defines function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, name, value):
    """adds attributes if possible"""
    if hasattr(obj, '__dict__'):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
