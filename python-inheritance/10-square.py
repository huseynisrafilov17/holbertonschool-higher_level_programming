#!/usr/bin/python3
'''
MyModule
'''
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    '''
    My Square class
    '''
    def __init__(self, size):
        super().__init__(size, size)
