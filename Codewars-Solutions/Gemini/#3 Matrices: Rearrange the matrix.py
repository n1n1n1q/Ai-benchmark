"""
returns -1 in all cases
"""

import itertools
import numpy as np


def rearr(matrix):
    n = len(matrix)

    # Generate all permutations of the rows
    permutations = itertools.permutations(matrix)

    # Convert each permutation to a numpy array for efficient determinant calculation
    for perm in permutations:
        perm_array = np.array(perm)

        # Check if determinant is 0
        if np.linalg.det(perm_array) == 0:
            return perm_array.tolist()  # Convert back to list of lists

    return -1


# working solution
def working_rearr(matrix):
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
