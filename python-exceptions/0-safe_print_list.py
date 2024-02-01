#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print(my_list[i], end="")
        except IndexError:
            i = i - 1
            break
    print()
    return i + 1

my_list = [1, 2, 3, 4, 5]
