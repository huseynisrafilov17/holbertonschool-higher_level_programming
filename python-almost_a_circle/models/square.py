#!/usr/bin/python3
'''
My module
'''
from rectangle import Rectangle


class Square(Rectangle):
    '''
    Square Class
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(x=x, y=y, id=id)
        self.size = size

    def __str__(self):
        c_n = self.__class__.__name__
        return "[{}] ({}) {}/{} - {}".format(c_n, self.id,
                                             self.x, self.y, self.width)

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
