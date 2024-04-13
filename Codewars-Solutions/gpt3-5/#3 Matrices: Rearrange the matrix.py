"""
solved at a "first" try with direct order on how to aproach problem
"""

import numpy as np
from itertools import chain, permutations


def rearr(matrix):
    n = len(matrix)

    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        return -1

    # Generate all possible permutations of the elements
    perms = permutations(chain(*matrix))

    for perm in perms:
        # Reshape the permutation into a square matrix
        perm_matrix = np.array(perm).reshape(n, n)

        # Calculate the determinant
        if np.linalg.det(perm_matrix) == 0:
            return perm_matrix.tolist()

    # If no rearrangement gives a determinant of 0, return -1
    return -1


# Test the function
matrix = [[2, 1], [3, 6]]
print(rearr(matrix))
