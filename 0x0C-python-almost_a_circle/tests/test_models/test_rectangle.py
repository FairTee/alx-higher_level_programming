#!/usr/bin/python3
"""Test cases"""

import unittest.mock
import io
import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangleMethods(unittest.TestCase):
    def test_area(self):
        """Test the area method of Rectangle."""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """Test the display method of Rectangle."""
        r = Rectangle(5, 3, 2, 2)
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), "\n" * 2 + "  #####\n  #####\n  #####\n")

    def test_update_args(self):
        """Test the update method of Rectangle with *args."""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(10, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (10) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test the update method of Rectangle with **kwargs."""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=10, width=2, height=3, x=4, y=5)
        self.assertEqual(str(r), "[Rectangle] (10) 4/5 - 2/3")

    def test_to_dictionary(self):
        """Test the to_dictionary method of Rectangle."""
        r = Rectangle(1, 2, 3, 4, 5)
        expected_dict = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_str(self):
        """Test the __str__ method of Rectangle."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_to_csv_row(self):
        """Test the to_csv_row method of Rectangle."""
        r = Rectangle(1, 2, 3, 4, 5)
        expected_row = [5, 1, 2, 3, 4]
        self.assertEqual(r.to_csv_row(), expected_row)

    def test_create_from_csv_row(self):
        """Test the create_from_csv_row method of Rectangle."""
        row = [3, 4, 5, 1, 2]
        created_rectangle = Rectangle.create_from_csv_row(row)
        expected_rectangle = Rectangle(5, 1, 2, 3, 4)
        self.assertEqual(str(created_rectangle), str(expected_rectangle))


if __name__ == '__main__':
    unittest.main()
