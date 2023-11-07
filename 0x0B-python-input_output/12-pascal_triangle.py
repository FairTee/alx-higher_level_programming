#!/usr/bin/python3
"""Contains the pascal triangle function"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.

    Example:
        pascal_triangle(5) returns:
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # Each row starts with 1.
        if triangle:
            prev_row = triangle[-1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # Each row ends with 1.
        triangle.append(row)

    return triangle
