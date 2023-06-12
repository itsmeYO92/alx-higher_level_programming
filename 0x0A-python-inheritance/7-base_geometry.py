#!/usr/bin/python3
""" is_same_class function to compare two classes"""


class BaseGeometry():
    """ list the attributes and methos of an object"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) not in [int, float]:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
