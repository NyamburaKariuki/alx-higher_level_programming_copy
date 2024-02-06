#!/usr/bin/python3
"""reps a function that changes a string to Json"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of a string
    args: my_obj-string to convert"""
    return json.dumps(my_obj)
