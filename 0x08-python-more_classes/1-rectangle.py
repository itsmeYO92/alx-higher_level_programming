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

        self.height = height
        self.width = width

    @property
    def width(self):
        return (self.width)

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.height = value

    @property
    def height(self):
        return (self.height)

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.height = value
