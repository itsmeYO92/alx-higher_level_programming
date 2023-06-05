#!/usr/bin/python3
"""
This is '1-rectangle' module.
Functions and Classes:
    class Rectangle()
"""


class Rectangle:
    """representing a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
            my_str += str(self.print_symbol) * self.__width + "\n"
        my_str += str(self.print_symbol) * self.__width
        return my_str

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
             return rect_1
