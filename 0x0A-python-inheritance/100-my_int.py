#!/usr/bin/python3
""" Square module defines a square by its size """


class MyInt(int):
    """ class MyInt inherints from int"""
    def __eq__(self, other):
        return self.real != other.real

    def __ne__(self, other):
        return self.real == other.real
