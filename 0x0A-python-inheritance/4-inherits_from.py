#!/usr/bin/python3
""" is_same_class function to compare two classes"""


def inherits_from(obj, a_class):
    """ list the attributes and methos of an object"""
    if issubclass(obj.__class__, a_class):
        if obj.__class__ is not a_class:
            return True
    return False
