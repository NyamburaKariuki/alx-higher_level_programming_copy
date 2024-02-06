#!/usr/bin/python3
"""defines a function that converts a JSON string to python data structure"""


import json


def from_json_string(my_str):
    """returns an object represnted by JSON string"""
    return json.loads(my_str)
    
