#!/usr/bin/python3
""" update a text file """


def append_after(filename="", search_string="", new_string=""):
    """ append a string after a line """
    with open(filename, mode="r") as f:
        lines = f.readlines()
    f.close()

    with open(filename, mode="w") as f:
        for line in lines:
            f.writelines(line)
            if line.find(search_string) != -1:
                f.writelines(new_string)
    f.close()
