#!/usr/bin/python3
"""Task 3"""


class Square:
    """Square Class"""
    def __init__(self, size=0):

        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError

        if size < 0:
            print("size must be >= 0", end="")
            raise ValueError

        self.__size = size

    def area(self):
        return self.__size ** 2
