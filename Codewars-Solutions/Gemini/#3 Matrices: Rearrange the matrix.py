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
