#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            new_string = new_string + chr(ord(i) - 32)
        else:
            new_string = new_string + i
    print("{}".format(new_string))
