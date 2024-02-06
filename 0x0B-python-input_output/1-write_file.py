#!/usr/bin/python3
"""contains a functions that writes text to a file"""


def write_file(filename="", text=""):
    """writes text to a file and returns the number of characters
    args: filename-file to write
    text-string to write"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
