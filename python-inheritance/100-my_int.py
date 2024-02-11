#!/usr/bin/python3
'''
My module
'''


class MyInt(int):
    '''
    My int
    '''
    def __eq__(self, other):
        return self^other != 0
    def __ne__(self, other):
        return self^other == 0
