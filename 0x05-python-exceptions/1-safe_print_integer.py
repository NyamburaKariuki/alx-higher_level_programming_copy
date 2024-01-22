#!/usr/bin/python3
def safe_print_integer(value):
    '''prints an integer with "{:d}".format()
    value can be any type (integer, string, etc.)
    Returns True if value has been correctly
    printed (it means the value is an integer)
    Otherwise, returns False'''

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
