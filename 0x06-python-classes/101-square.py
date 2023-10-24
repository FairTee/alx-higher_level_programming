#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        output = ""
        if self.__size == 0:
            return output
        output += "\n" * self.__position[1]
        for _ in range(self.__size):
            output += " " * self.__position[0] + "#" * self.__size + "\n"
        return output.rstrip()


if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)
    print("--")
    my_square = Square(5, (4, 1))
    print(my_square)
