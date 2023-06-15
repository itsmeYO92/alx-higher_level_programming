#!/usr/bin/python3
""" Square module defines a square and inherits from Rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ rectangle class inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
                .format(self.id, self.x, self.y,\
                self.height)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.is_valide_int(**{"size": size})
        self.width = size
        self.height = size
