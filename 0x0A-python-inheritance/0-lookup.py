#!/usr/bin/python3

def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the
        names of attributes and methods of the object.
    """
    return dir(obj)


class MyClass1(object):
    """ My first class """
    pass


class MyClass2(object):
    """ My second class """
    my_attr1 = 3

    def my_meth(self):
        """ My method """
        pass


if __name__ == "__main__":
    print("Documentation for lookup function:")
    print(lookup.__doc__)

    print("Documentation for MyClass1:")
    print(MyClass1.__doc__)

    print("Documentation for MyClass2.my_meth:")
    print(MyClass2.my_meth.__doc__)

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
