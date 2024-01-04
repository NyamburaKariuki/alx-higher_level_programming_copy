#!/usr/bin/python3


def remove_char_at(str, n):
    '''copies string and remove character at n index'''
    if n < 0:
        return (str)
    else:
        new_string = str[:n] + str[n+1:]
        return (new_string)
