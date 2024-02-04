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
        self.size = size

    def area(self):
        '''Calculates the area of square'''
        return self.__size ** 2

    def __eq__(self, other):
        '''Equal comparison'''
        return self.area() == other.area()

    def __ne__(self, other):
        '''Not equal comparison'''
        return self.area() != other.area()

    def __lt__(self, other):
        '''Less than comparison'''
        return self.area() < other.area()

    def __le__(self, other):
        '''Less than or equal comparison'''
        return self.area() <= other.area()

    def __gt__(self, other):
        '''Greater than comparison'''
        return self.area() > other.area()

    def __ge__(self, other):
        '''Greater than or equal comparison'''
        return self.area() >= other.area()

    @property
    def size(self):
        '''size getter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        size setter

        Args:
            value: value of the size
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
