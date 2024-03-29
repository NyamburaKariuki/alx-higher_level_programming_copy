#!/usr/bin/python3
"""Defines a function that multiplies 2 matrices by using the module NumPy"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        matrix: the product of the two matrices.
    """
    # m_a = ([1, 2], [3, 4])
    # m_b = [[1, 2], [3, 4]]
    return np.matmul(m_a, m_b)
