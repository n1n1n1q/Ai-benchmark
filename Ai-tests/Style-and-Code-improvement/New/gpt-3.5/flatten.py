"""
Flatten gtp-3.5
"""

def flatten(lst):
    if not isinstance(lst, list):
        return lst
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        elif item is not None:
            result.append(item)
    return result
