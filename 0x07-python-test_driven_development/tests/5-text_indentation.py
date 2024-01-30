#!/usr/bin/python3
"""text indentation"""


def text_indentation(text):
    """prints a text with 2 new lines\
    after each of these characters: ., ? and :
    Args: test(string)"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for ch in ".:?":
        text = (ch + '\n\n').join([line.strip(" ") for line in text.split(ch)])
    print(text, end="")
