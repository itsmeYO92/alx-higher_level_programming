#!/usr/bin/python3
"""
This is '1-rectangle' module.
Functions and Classes:
    class Rectangle()
"""


class Rectangle:
    """representing a rectangle"""

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.area() == 0:
            return (0)
        return (2 * self.__height + 2 * self.__width)

    def __str__(self):
        if self.area() == 0:
            return ""
        my_str = ""
        for i in range(0, self.__height - 1):
            my_str += "#" * self.__width + "\n"
        my_str += "#" * self.__width
        return my_str
