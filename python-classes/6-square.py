#!/usr/bin/python3
"""Task 3"""


def is_int(value):
    """Check Size"""

    if type(value) is not int:
        raise TypeError("size must be an integer")
        return False

    if value < 0:
        raise ValueError("size must be >= 0")
        return False

    return True


def check_tuple(position):
    """Check Tuple"""

    if type(position) is not tuple:
        raise TypeError("position must be a tuple of 2 positive integers")
        return False

#    if type(position[0]) is not int or type(position[1] is not int):
#        raise TypeError("position must be a tuple of 2 positive integers")
#        return False

    if position[0] < 0 or position[1] < 0:
        raise TypeError("position must be a tuple of 2 positive integers")
        return False

    return True


class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        if is_int(size):
            self.__size = size
        if check_tuple(position):
            self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if is_int(value):
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if check_tuple(position):
            self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
