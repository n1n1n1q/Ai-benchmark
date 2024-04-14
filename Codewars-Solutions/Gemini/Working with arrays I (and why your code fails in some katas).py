def without_last(lst):
    """Returns a copy of the list without its last element.

    Args:
        lst: The input list.

    Returns:
        A new list containing all elements except the last one from the input list.
    """

    # Create a copy of the list to avoid modifying the original.
    return lst[:-1]
