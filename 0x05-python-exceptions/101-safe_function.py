#!/usr/bin/python3
def safe_function(fct, *args):
    '''executes a function safely
    fct will be always a pointer to a function
    Returns the result of the function
    Otherwise, returns None
    print the exception to stderr
    args, function arguments'''
    import sys
    try:
        result = fct(*args)
        return result
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
