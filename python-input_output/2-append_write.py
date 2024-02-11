#!/usr/bin/python3
'''
Module that has a function to write text into a file
'''


def append_write(filename="", text=""):
    '''
    write_file writes text into a file
    Args:
        filename: file name
        text: text
    '''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
