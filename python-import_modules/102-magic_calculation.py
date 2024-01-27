def magic_calculation(a, b):
    if a < b:
        from magic_calculation_102 import add, sub
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    from magic_calculation_102 import sub
    return sub(a, b)
