"""
Flatten
"""


def flatten(lst):
    return (
        [
            item
            for sublist in lst
            for item in (flatten(sublist) if isinstance(sublist, list) else [sublist])
            if item is not None
        ]
        if isinstance(lst, list)
        else lst
    )
