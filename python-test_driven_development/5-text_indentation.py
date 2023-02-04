#!/usr/bin/python3
"""
Task 5
"""


def text_indentation(text):
    """ Text identation"""
    if text is None or type(text) is not str:
        raise TypeError("text must be a string")

    newline = False

    for char in text:
        if newline:
            newline = False
            continue
        print(char, end="")
        if char in ['.', '?', ':']:
            print()
            newline = True
