#!/usr/bin/python3
"""Task 2"""


class Square:
    """Square CLass"""
    def __init__(self, size=0):

        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError

        if size < 0:
            print("size must be >= 0", end="")
            raise ValueError

        self.__size = size
