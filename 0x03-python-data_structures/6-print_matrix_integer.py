#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for element in x:
            if x[-1] == element:
                print("{:d}".format(x[-1]), end="")
            else:
                print("{:d}".format(element), end=" ")
        print()
