#!/usr/bin/python3
"""
Task 2
"""


def matrix_divided(matrix, div):
    """Matrix Divided"""

    if matrix is None or type(matrix) is not list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if div is None or type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    len_rows = len(matrix[0])

    for row in matrix:
        if len(row) != len_rows:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(
                        "matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = matrix.copy()

    for i in range(len(new_matrix)):
        new_matrix[i] = matrix[i].copy()

    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] = round(new_matrix[i][j] / div, 2)

    return new_matrix
