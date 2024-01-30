#!/usr/bin/python3
"""module defines a locked class"""


class LockedClass:
    """that prevents the user from dynamically creating new\
    instance attributes, except if the new instance attribute\
    called first_name."""
    __class__ = ["first_name"]
