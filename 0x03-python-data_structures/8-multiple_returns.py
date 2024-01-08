#!/usr/bin/python3


def multiple_returns(sentence):
    '''returns string length and first character'''
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
