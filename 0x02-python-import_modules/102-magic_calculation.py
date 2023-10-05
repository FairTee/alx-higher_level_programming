#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        def add(x, y):
            return x + y

        def sub(x, y):
            return x - y

        c = 0
        for i in range(4, 7):
            c = add(c, i)
        return c
    return sub(a, b)
