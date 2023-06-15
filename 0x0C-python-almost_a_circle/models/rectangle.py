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
                raise ValueError("{} must be > 0".format(key))

            if key in ["x", "y"] and arg < 0:
                raise ValueError("{} must be > 0".format(key))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.is_valide_int(**{"width": width})
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.is_valide_int(**{"height": height})
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.is_valide_int(**{"x": x})
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.is_valide_int(**{"y": y})
        self.__y = y

    def area(self):
        """ returns the area of the rectangle """
        return self.__height * self.__width

    def display(self):
        """ prints a triangle with '#' character """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
                .format(self.id, self.__x, self.__y,\
                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Update a rectangle """
        if args:
           keys = ["id", "width", "height", "x", "y"]
           i = 0
           for arg in args:
               setattr(self, keys[i], arg)
               i += 1

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
