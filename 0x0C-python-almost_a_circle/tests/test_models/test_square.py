#!/usr/bin/python3>
"""Defines unittests for models/square.py."""


import unittest
from models.square import Square
from models.rectangle import Rectangle

class TestSquareMethods(unittest.TestCase):
    def test_init(self):
        """Test the initialization of Square."""
        s = Square(5, 2, 3, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 10)


    def test_update_args(self):
        """Test the update method of Square with *args."""
        s = Square(1, 1, 1, 1)
        s.update(10, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (10) 3/4 - 2")

    def test_update_kwargs(self):
        """Test the update method of Square with **kwargs."""
        s = Square(1, 1, 1, 1)
        s.update(id=10, size=2, x=3, y=4)
        self.assertEqual(str(s), "[Square] (10) 3/4 - 2")

    def test_to_dictionary(self):
        """Test the to_dictionary method of Square."""
        s = Square(1, 2, 3, 4)
        expected_dict = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_str(self):
        """Test the __str__ method of Square."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_to_csv_row(self):
        """Test the to_csv_row method of Square."""
        s = Square(1, 2, 3, 4)
        expected_row = [4, 1, 2, 3]
        self.assertEqual(s.to_csv_row(), expected_row)

if __name__ == '__main__':
    unittest.main()
