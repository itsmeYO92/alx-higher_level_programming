#!/usr/bin/python3
"""
   1-rectangle module - a module that defines a rectangle
   class Rectangle()
"""


class Rectangle:
    """
       Rectangle class definitioni - defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
            initialisation function
        """
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

    @proprety
    def width(self):
        """
           width getter
        """
        return (self.width)

    @width.setter
    def width(self, value):
        """
            width setter
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.height = value

    @proprety
    def height(self):
        """
           height getter
        """
        return (self.height)

    @height.setter
    def height(self, value):
        """
           height setter
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.height = value
