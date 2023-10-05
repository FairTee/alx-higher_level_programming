#!/usr/bin/python3

if __name__ == '__main__':
    def magic_calculation(a, b):
        if a < b:
            from magic_calculation_102 import add
            c = 0
            for i in range(4, 7):
                c = add(c, i)
            return c
        from magic_calculation_102 import sub
        return sub(a, b)
