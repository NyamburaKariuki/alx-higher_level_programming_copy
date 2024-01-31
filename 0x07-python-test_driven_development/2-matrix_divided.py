#!/usr/bin/python3
"""defines a function that divide elements of a matrix"""


def matrix_divided(matrix, div):
    """divide all elements of a matrix by div
    Args: Matrix-given matrix
        div: number to divide with"""

    row = None
    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
        of integers/floats")
    for x in matrix:
        if not x or not isinstance(x, list):
            raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
        for y in x:
            if not isinstance(y, int) and not isinstance(y, float):
                raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
        if row is None:
            row = len(x)
        if row != len(x):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(y/div, 2) for y in x] for x in matrix]
    return new_matrix
