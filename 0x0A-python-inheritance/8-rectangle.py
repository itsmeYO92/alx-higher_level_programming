#!/usr/bin/python3
""" is_same_class function to compare two classes"""


BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    """ list the attributes and methos of an object"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) not in [int, float]:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
