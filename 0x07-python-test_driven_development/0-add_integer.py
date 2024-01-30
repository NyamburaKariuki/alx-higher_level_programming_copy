#!/usr/bin/python3
"""does integers additions"""


def add_integer(a, b=98):
    """adds 2 integers
    args: a must be an integer or float
        : b (int 0r float
    returns the sum of the two"""

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer of float")
    return (int(a) + int(b))
