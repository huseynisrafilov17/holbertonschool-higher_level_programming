#!/usr/bin/python3
'''Square with private size attribute and check'''


class Square:
    '''Gets size as its attribute'''
    def __init__(self, size=0):
        '''
        __init__ gets attribute and sets it

        Args:
            size: size of square
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
