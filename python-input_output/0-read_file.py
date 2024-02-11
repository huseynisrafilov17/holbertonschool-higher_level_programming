#!/usr/bin/python3
'''
This module has a function for reading from a file
'''

def read_file(filename=""):
    '''
    read_file reads from a file and prints it
    Args:
        filename: file name
    '''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
