#!/user/bin/python3
""" base module- manage ids """


import json
import csv


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

    @classmethod
    def create(cls, **dictionary):

        from models.square import Square
        from models.rectangle import Rectangle


        if dictionary:
            if cls is Base:
                dummy = cls()
            elif cls is Square:
                dummy = cls(1)
            elif cls is Rectangle:
                dummy = cls(1,1)
            else:
                return None

            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        instance_list = []

        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, "r", encoding="UTF-8") as f:
                saved_json = f.read()
        except FileNotFoundError:
            return instance_list

        json_list = Base.from_json_string(saved_json)
        if json_list is None:
            return instance_list

        for __dict in json_list:
            instance_list.append(cls.create(**__dict))
        return instance_list

    @classmethod
    def load_from_csv(cls):
        file_name = cls.__name__ + ".csv"
        if file_name == "Rectangle.csv":
            keys = ["id", "width", "height", "x", "y"]
        else:
            keys = ["id", "size", "x", "y"]

        ilist = []
        try:
            with open(file_name, "r", encoding="UTF-8", newline="") as f:
                csv_content = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

        except FileNotFoundError:
            return ilist

        for line in csv_content:
            d = {}
            for key in keys:
                d[key] = int(line[keys.index(key)])
                ilist.append(cls.create(**d))

        return ilist
