#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for idx, num in enumerate(line):
            print("{:d}".format(num),
                  end="\n" if idx == len(line) - 1 else " ")
