#!/usr/bin/python3
def safe_print_integer_err(value):
    ''' prints an integer
    Returns True if value has been correctly printed
    Otherwise, returns False and prints\
    in stderr the error precede by Exception:
    You have to use try: / except:
    You are not allowed to use type()'''
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
