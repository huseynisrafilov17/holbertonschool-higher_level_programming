#!/usr/bin/python3
'''
My module
'''


class Base:
    '''
    Base Class
    Args:
        __nb_objects: variable
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            id = __nb_objects
