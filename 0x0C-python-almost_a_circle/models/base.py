#!/user/bin/python3
""" base module- manage ids """


import json


class Base():
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(my_obj):
        """return JSON representation of an object"""
        if my_obj is None:
            return("[]")
        return json.dumps(my_obj)

