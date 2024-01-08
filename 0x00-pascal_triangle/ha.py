#!/usr/bin/python3
"""
0-pascal_triangle
"""

n = input('Enter the value of n:\n')
n = int(n)

while n <= 0:
    n = input('Enter a value higher than 0:\n')
    n = int(n)

def pascal_triangle(n):
    """
    Returns a list of integers representing the Pascal Triangle of n.
    Returns an empty list if n <= 0.
    """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = [1]  # First element in every row is 1

        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)  # Last element in every row is 1

        triangle.append(row)

    return triangle

def print_pascal_triangle(triangle):
    """
    Prints the Pascal Triangle in a symmetrically formatted way.
    """
    max_width = len(' '.join(map(str, triangle[-1])))  # Maximum width needed for any row

    for row in triangle:
        # Center-align the numbers and pad with leading spaces
        formatted_row = ' '.join(map(str, row)).center(max_width)
        print(formatted_row)

triangle = pascal_triangle(n)
print_pascal_triangle(triangle)
