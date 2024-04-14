def median_from_n_arrays(arrays):
    """
    Finds the median value from a list of sorted arrays.

    Args:
        arrays: A list of sorted arrays of integers.

    Returns:
        The median value of all the elements in the combined lists, or None if all arrays are empty.
    """

    # Combine all elements into a single sorted list (excluding empty arrays)
    combined_list = []
    for arr in arrays:
        combined_list.extend(arr)
    combined_list.sort()

    # Handle empty arrays as a special case
    if not combined_list:
        return None

    # Find the median element based on the total length
    total_elements = len(combined_list)
    median_index = total_elements // 2

    # Return the middle element for odd number of elements
    if total_elements % 2 == 1:
        return combined_list[median_index]
    else:
        # Return the average of the middle two elements for even number
        return (combined_list[median_index - 1] + combined_list[median_index]) / 2
