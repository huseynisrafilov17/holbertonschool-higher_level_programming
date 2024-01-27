def magic_calculation(a, b):
    add = from magic_calculation_102 import add
    sub = from magic_calculation_102 import sub
    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return c
    return sub(a, b)
