#!/usr/bin/python3
'''
A function to add two integers

a and b must be integer or floats.
'''


def add_integer(a, b=98):
    '''add_integer adds two integers
    Args:
        a, b: integer'''
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
