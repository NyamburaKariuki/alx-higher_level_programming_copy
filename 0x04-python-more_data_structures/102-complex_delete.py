#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    '''deletes keys with a specific value in a dictionary'''
    list_keys = list(a_dictionary.keys())
    for k in list_keys:
        if value == a_dictionary.get(k):
            del a_dictionary[k]
    return a_dictionary
