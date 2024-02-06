#!/usr/bin/python3
'''
MyModule
'''


def inherits_from(obj, a_class):
    '''
    inherits_from checks if obj is inherited from a_class

    Args:
        obj: object
        a_class: class
    '''
    return isinstance(obj, a_class)
