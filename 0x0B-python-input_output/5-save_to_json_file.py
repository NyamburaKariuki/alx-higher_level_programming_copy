#!/usr/bin/python3
"""fn that writes to a text file using JSON rep"""


import json


def save_to_json_file(my_obj, filename):
    """"writes to a txt file using JSON rep
    args: my_obj- string to write
        filename: file to write to"""
    with open(filename, 'w', encoding="utf-8") as f:
        o_bject = json.dumps(my_obj)
        f.write(o_bject)
        f.close()
