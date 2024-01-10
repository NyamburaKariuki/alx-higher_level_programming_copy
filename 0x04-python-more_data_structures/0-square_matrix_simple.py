#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    '''multiplies the elements of a matrix, without\
     modifying the original matrix'''
    copy_matrix = list.copy(matrix)
    for x in range(len(matrix)):
        copy_matrix[x] = list(map(lambda y: y**2, matrix[x]))
    return copy_matrix
