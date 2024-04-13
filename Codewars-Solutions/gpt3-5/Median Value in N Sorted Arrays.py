"""
first and the most successful solution. Works correctly but exceeds time out.
"""


def median_from_n_arrays(arrays):
    merged = []
    for arr in arrays:
        merged.extend(arr)
    merged.sort()
    n = len(merged)
    if n % 2 == 0:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2
    else:
        return merged[n // 2]
