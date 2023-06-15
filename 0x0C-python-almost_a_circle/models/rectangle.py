#!/usr/bin/python3
""" rectangle module: defines a rectangle """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class: defines a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__args = {}
        self.__args = {"width": width, "height": height, "x": x, "y": y}
        self.is_valide_int(**self.__args)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def is_valide_int(self, **kwargs):
        for key, arg in kwargs.items():
            if type(arg) is not int:
                raise TypeError("{} must be an integer".format(key))
            if key in ["width", "height"] and arg <= 0:
                raise ValueError("{} must be bigger than 0".format(key))
