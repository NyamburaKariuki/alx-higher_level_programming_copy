#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''function that replaces an element in a list at a specific\
    position without modifying the original list
    If idx is negative, the function should\
    return a copy of the original list
    If idx is out of range (> of number of element\
    in my_list), the function should return a copy of the original list
    You are not allowed to import any module
    '''

    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return (new_list)
