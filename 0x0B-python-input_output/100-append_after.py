#!/usr/bin/python3
"""contains function that inserts a lne of text\
after serching for a certain string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text if a certain string esxist
    args: filename -file to write
    search_string- string to search for
    new_string- string to write"""
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    with open(filename, 'w', encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')

