#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    NewMatrix = []
    for line in matrix:
        NewMatrix.append(list(map(lambda x: x * x, line)))
    return NewMatrix
