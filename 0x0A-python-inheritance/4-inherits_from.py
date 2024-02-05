#!/usr/bin/python3
"""module defines a function that checks if obj is inherited from class"""


def inherits_from(obj, a_class):
    """Returns true if an object is an instance\
    of a clss that inherited from a class"""

    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
