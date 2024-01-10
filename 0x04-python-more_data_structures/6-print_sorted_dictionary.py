#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    '''prints a dictionary by ordered keys'''
    sorted_dict = dict(sorted(a_dictionary.items()))
    print(sorted_dict, end="\n")
