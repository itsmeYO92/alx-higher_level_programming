#!/usr/bin/python3
"""
    divide matrix module
"""


def matrix_divided(matrix, div):
    """
       return new matrix divided by div
    """

    new_matrix = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if type(matrix) is not list or type (matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size = len(matrix[0])
    for i in matrix:
        line = []
        if len(i) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for num in i:
            if type(num) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            line.append(float(round(num / div, 2)))
        new_matrix.append(line)
    return (new_matrix)
