#!/usr/bin/python3
"""Task 0"""

from models.base import Base


def check_width(width):
    if type(width) is not int:
        raise TypeError("width must be an integer")
    if width <= 0:
        raise ValueError("width must be > 0")


def check_height(height):
    if type(height) is not int:
        raise TypeError("height must be an integer")
    if height <= 0:
        raise ValueError("height must be > 0")


def check_x(x):
    if type(x) is not int:
        raise TypeError("x must be an integer")
    if x < 0:
        raise ValueError("x must be >= 0")


def check_y(y):
    if type(y) is not int:
        raise TypeError("y must be an integer")
    if y < 0:
        raise ValueError("y must be >= 0")


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        check_width(width)
        check_height(height)
        check_x(x)
        check_y(y)

        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        check_width(value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        check_height(value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        check_x(value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        check_y(value)
        self.__y = value
