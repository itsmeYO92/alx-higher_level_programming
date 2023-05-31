#!/usr/bin/python3
""" This module defines a Square class. """


class Square:
    """class representing a square"""

    def __init__(self, size=0):
        self.__size = size

    @size.setter
    def size(self, value):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area of a square"""

        return ((self.__size) ** 2)

    @property
    def size(self):
        return self.__size
