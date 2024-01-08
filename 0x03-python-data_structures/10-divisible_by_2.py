#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    '''finds all multiples of 2 in a list.
    Return a new list with True or False, depending\
    on whether the integer at the same position in the\
    original list is a multiple of 2
    The new list should have the same size as the original list
    '''
    new = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return new
