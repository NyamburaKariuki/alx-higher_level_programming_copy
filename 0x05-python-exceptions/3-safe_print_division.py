#!/usr/bin/python3
def safe_print_division(a, b):
    '''divides 2 integers and prints the result
    a and b are integers
    The result of the division should print on the finally:
    Returns the value of the division, otherwise: None
    You have to use "{}".format() to print the result'''

    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
