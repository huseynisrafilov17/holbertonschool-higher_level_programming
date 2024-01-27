#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n < len(str):
        new_string = ""
        new_string += str[0:n]
        if n != len(str) - 1:
            new_string += str[n+1:]
        return new_string
    return str
