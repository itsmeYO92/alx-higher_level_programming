#!/usr/bin/python3
"""square class"""


class Square:
    """init"""

    @size.setter
    def size(self, value):
        if type(size) is not int:
            raise TypeErrror("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return ((self.__size) ** 2)

    def __init__(self, size=0):
        self.size = size
