#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ''' prints the first x elements of a list and only integers
    other type of value in the list must be skipped (in silence)
    You have to use "{:d}".format() to print an integer'''

    result = 0
    for i in range(x):
        if isinstance(my_list[i], int):
            try:
                print(my_list[i], end='')
            except IndexError:
                break
        else:
            continue
    result += 1
    print()
    return result
