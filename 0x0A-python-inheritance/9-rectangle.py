#!/usr/bin/python3
""" is_same_class function to compare two classes"""


BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    """ list the attributes and methos of an object"""
    def area(self):
        return self.__width * self.__height

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return "[Retangle] {}/{}".format(self.__width, self.__height)
