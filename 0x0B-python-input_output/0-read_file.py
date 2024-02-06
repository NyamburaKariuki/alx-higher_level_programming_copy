#!/usr/bin/python3
"""module that defines a fucntion for reading a text file"""


def read_file(filename=""):
    """reads a text file and prints to stdout"""

    with open(filename, 'r', encoding="utf-8") as a_file:
        """opens a file name
            args: Filename-file
                mode, encoding"""
        read_file = a_file.read()
        print(read_file, end='')
