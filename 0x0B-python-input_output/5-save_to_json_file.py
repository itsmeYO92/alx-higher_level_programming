#!/usr/bin/python3
""" write file module: write a file """


import json
def save_to_json_file(my_obj, filename):
    """ write a text file """
    with open(filename, mode="w") as f:
        nb = json.dump(my_obj, f)
    f.close()
    return nb
