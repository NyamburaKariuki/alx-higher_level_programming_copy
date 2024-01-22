#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ''' prints the first x elements of a list and only integers
    other type of value in the list must be skipped (in silence)
    You have to use "{:d}".format() to print an integer'''

    count = 0
    for item in range(x):
        try:
            print("{:d}".format(my_list[item], end=""))
            count += 1
        except (TypeError, ValueError):
            continue
    print ()
    return count
