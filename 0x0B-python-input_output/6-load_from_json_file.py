#!/usr/bin/python3
""" write file module: write a file """


import json


def load_from_json_file(filename):
    """ write a text file """
    with open(filename, mode="r") as f:
        nb = json.load(f)
    f.close()
    return nb
