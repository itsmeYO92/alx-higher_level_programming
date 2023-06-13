#!/usr/bin/python3
""" write file module: write a file """


def append_write(filename="", text=""):
    """ write a text file """
    with open(filename, mode="a", encoding="utf-8") as f:
        nb = f.write(text)
    f.close()
    return nb
