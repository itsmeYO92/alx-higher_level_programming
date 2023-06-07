#!/usr/bin/python3
""" divide matrix module """


def print_square(size):
    """ say_my_name: prints the full name"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
