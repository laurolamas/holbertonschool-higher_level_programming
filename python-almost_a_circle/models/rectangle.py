#!/usr/bin/python3
"""Task 0"""

from models.base import Base
from models.check_input import *


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

    def area(self):
        """that returns the rectangle area"""
        return (self.height * self.width)

    def display(self):
        """ Display """

        for y in range(self.y):
            print()

        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            if i != self.height - 1:
                print()
        print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}"\
               f" - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ Update """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

        if args is not None and len(args) > 0:
            return

        attributes = ["id", "width", "height", "x", "y"]

        if kwargs is not None:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

        
    def to_dictionary(self):
        return self.__dict__
