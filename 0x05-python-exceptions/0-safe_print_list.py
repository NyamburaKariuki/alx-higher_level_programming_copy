#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''prints x elements of a list
    my_list contains inetegers, strings etc
    do not use len, you have to use try:/exceptions
    '''

    counter = 0
    for element in range(x):
        try:
            print(my_list[element], end="")
        except IndexError:
            break
        else:
            counter += 1
    print("")
    return counter
