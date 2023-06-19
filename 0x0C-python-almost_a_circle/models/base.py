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

    @classmethod
    def save_to_file(cls, list_objs):
        """ a class method that saves the json string to a file """
        file_name = cls.__name__ + ".json"
        list_dict = []

        if list_objs:
            for obj in list_objs:
                if isinstance(obj, Base):
                    list_dict.append(obj.to_dictionary())

        json_string = Base.to_json_string(list_dict)
        with open(file_name, "w") as f:
            f.write(json_string)
        f.close

    @staticmethod
    def from_json_string(json_string):
        """ returns a list of json string """

        if json_string is None:
            return []
        return json.loads(json_string)

