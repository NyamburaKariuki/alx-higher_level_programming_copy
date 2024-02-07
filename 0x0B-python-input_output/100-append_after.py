#!/usr/bin/python3
"""contains function that inserts a lne of text\
after serching for a certain string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text if a certain string esxist
    args: filename -file to write
    search_string- string to search for
    new_string- string to write"""
    lines = ""
    with open(filename, 'r') as f:
        for line in f:
            lines += line
            if search_string in line:
                lines += new_string
    with open(filename, 'w') as f:
        f.write(lines + '\n')
