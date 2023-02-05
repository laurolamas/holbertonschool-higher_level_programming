#!/usr/bin/python3
"""Task 0"""


def check_width(width):
    if type(width) is not int:
        raise TypeError("width must be an integer")
    if width < 0:
        raise ValueError("width must be >= 0")

    return True


def check_height(height):
    if type(height) is not int:
        raise TypeError("height must be an integer")
    if height < 0:
        raise ValueError("height must be >= 0")

    return True


class Rectangle:
    """Rectangle Class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if check_width(width):
            self.__width = width
        if check_height(height):
            self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if check_width(value):
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if check_height(value):
            self.__height = value

    def area(self):
        """that returns the rectangle area"""
        if 0 in [self.height, self.width]:
            return 0
        return (self.height * self.width)

    def perimeter(self):
        """that returns the rectangle perimeter"""
        if 0 in [self.height, self.width]:
            return 0
        return (2 * (self.height + self.width))

    def __str__(self):
        if 0 in [self.height, self.width]:
            return ""
        output = ""
        for i in range(self.height):
            for j in range(self.width):
                output += str(self.print_symbol)
            if i != self.height - 1:
                output += '\n'

        return output

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        del self
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):

        if rect_1 is None or not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if rect_2 is None or not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    def square(cls, size=0):
        return Rectangle(size, size)
