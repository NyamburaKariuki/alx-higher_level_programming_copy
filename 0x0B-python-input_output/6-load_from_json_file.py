#!/usr/bin/python3
"""fn that creates a python project from Json file"""


import json


def load_from_json_file(filename):
    """creates an objcet from a json file
    args: filename-json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
