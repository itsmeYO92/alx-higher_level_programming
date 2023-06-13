#!/usr/bin/python3
""" class  to json module """


def class_to_json(obj):
    """ dictionary representation for json of an object """
    new_dict = {}
    for i in dir(obj):
        if not (i.startswith("__") or callable(getattr(obj, i))):
            new_dict[i] = getattr(obj, i)

    return new_dict
