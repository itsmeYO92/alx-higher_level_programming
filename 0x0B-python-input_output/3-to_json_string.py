#!/usr/bin/python3
""" write file module: write a file """


import json


def to_json_string(my_obj):
    """ write a text file """
    return json.dumps(my_obj)
