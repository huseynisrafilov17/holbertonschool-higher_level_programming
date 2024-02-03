#!/usr/bin/python3
'''Square with private size attribute'''


class Square:
    '''Gets size as its attribute'''
    def __init__(self, size):
        '''
        __init__ gets attribute and sets it

        Args:
            size: size of square
        '''
        self.__size = size
