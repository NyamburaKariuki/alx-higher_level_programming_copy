#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    '''returns a new dictionary with all values multiplied by 2'''
    valuez = a_dictionary.values()
    keysha = a_dictionary.keys()
    n_valuez = [x * 2 for x in valuez]
    for k, v in zip(keysha, n_valuez):
        print("{0}: {1}".format(k, v))
