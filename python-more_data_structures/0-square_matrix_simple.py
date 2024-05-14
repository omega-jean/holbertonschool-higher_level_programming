#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for i in matrix:
        squared_row = []
        for j in i:
            squared_row.append(j ** 2)
        squared_matrix.append(squared_row)
    return squared_matrix
