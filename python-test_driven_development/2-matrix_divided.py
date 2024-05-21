#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) != list or matrix == []:
        raise TypeError("matrix must be a matrix\
                (list of lists) of integers/floats")

    first_row_length = len(matrix[0])

    for row in matrix:
        if len(row) != first_row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)

    return new_matrix
