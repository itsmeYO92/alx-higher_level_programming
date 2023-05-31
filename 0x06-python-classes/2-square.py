#!/usr/bin/python3
"""square class"""


class Square:
    """init"""
    def __init__(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
