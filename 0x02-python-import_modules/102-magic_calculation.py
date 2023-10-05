#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        add = __import__('magic_calculation_102').add
        sub = __import__('magic_calculation_102').sub
        c = 0
        for i in range(4, 7):
            c = add(c, i)
        return c
    return sub(a, b)
