#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    
    new_matrix = []
    for item in matrix:
        new_item = list(map(lambda x: X**2, item))
        new_matrix.append(new_item)

    return new_matrix
