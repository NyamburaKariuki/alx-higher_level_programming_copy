#!/usr/bin/python3


def search_replace(my_list, search, replace):
    ''' replace an element at an instance with another'''
    new_list = my_list.copy()
    for x in range(0, len(new_list)):
        if new_list[x] == search:
            new_list[x] = replace
    return new_list
