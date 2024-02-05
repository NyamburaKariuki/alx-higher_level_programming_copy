#!/usr/bin/python3
"""defines a class MyInt that inherits from int"""


class MyInt(int):
    """inverts operators == and !="""

    def __eq__(self, other):
        """inverts operator == to !="""
        return super(). __ne__(other)

    def __ne__(self, other):
        """inverts operator != to =="""
        return super().__eq__(other)
