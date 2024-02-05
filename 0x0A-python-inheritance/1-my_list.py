#!/usr/bin/python3
"""defines a class that inherits from list"""
class MyList(list):
    """class that inherits from list"""


    def print_sorted(self):
        """prints a list in sorted order"""
        print(sorted(self))
