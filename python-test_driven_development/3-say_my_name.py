#!/usr/bin/python3
'''
This module has a function that says your name.
'''


def say_my_name(first_name, last_name=""):
    '''
    say_my_name says your name

    Args:
        first_name: first name
        last_name: last name
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
