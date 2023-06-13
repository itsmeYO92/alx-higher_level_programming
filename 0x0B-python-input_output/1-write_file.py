#!/usr/bin/python3
""" write file module: write a file """


def write_file(filename="", text=""):
    """ write a text file """
    with open(filename, mode="w") as f:
        nb = f.write(text)
    f.close()
    return nb
