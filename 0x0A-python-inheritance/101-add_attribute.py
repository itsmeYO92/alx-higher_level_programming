#!/usr/bin/python3
""" Square module defines a square by its size """


def add_attribute(obj, attribute, value):
    """ class MyInt inherints from int"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
