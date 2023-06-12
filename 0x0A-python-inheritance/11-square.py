#!/usr/bin/python3
""" Square module defines a square by its size """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ class Square inherints from Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
