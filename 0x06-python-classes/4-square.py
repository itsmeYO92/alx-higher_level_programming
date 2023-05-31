#!/usr/bin/python3
"""
This module defines a Square class.

Square class:
- Represents a square with a given size.
- Provides methods to calculate the area
  and access/modify the size of the square.
"""


class Square:
    """class representing a square"""

    @size.setter
    def size(self, value):
        """setter"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area of a square"""

        return ((self.__size) ** 2)

    def __init__(self, size=0):
        """init"""
        self.__size = size

    @property
    def size(self):
        """getter"""
        return self.__size
