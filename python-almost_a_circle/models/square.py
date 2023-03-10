#!/usr/bin/python3
""" Square Class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        if args is not None and len(args) > 0:
            return

        attributes = ["id", "size", "x", "y"]

        if kwargs is not None:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ To Dictionary """
        dic = self.__dict__
        new_dic = {}
        for key, value in dic.items():
            if key == 'id':
                new_dic[key] = value
            elif key == '_Rectangle__width':
                new_dic['size'] = value
            elif key == '_Rectangle__height':
                pass
            else:
                new_dic[key[12:]] = value
        return new_dic
