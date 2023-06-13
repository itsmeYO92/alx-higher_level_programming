#!/usr/bin/python3
""" read file module: reads a file """


def read_file(filename=""):
    """ read a text file in UTF8 """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
    f.close()
