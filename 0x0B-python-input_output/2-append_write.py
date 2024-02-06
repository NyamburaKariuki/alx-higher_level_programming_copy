#!/usr/bin/python3
"""defines a function that appends text on a text file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    args: filename-file to append string
        text-string to append"""
    with open(filename, 'a', encoding="utf-8") as f:
        """open files and appends text
        return the number of characters appended"""
        return f.write(text)
