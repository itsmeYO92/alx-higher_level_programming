#!/usr/bin/python3
""" Student module """


class Student():
    """ a class represents a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        for i in dir(self):
            if not (i.startswith("__") or callable(getattr(self, i))):
                if attrs is None:
                    new_dict[i] = getattr(self, i)
                elif i in attrs:
                    new_dict[i] = getattr(self, i)

        return new_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, vlaue)
