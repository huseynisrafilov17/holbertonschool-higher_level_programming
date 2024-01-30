#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_un = 0
    myset = set(my_list)
    for i in myset:
        sum_un = sum_un + i
    return sum_un
