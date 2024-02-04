#!/usr/bin/python3
'''
This module includes a function that replace '.', ':', '?' with 2 new lines
'''
def text_indentation(text):
    '''
    text_indentation replaces '.', ':', '?' with 2 new lines

    Args:
        text: text
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(". ", "\n\n")
    text = text.replace(": ", "\n\n")
    text = text.replace("? ", "\n\n")
    print("{}".format(text), end="")
