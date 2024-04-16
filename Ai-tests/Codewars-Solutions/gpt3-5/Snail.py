def snail(snail_map):
    if not snail_map:
        return []
    result = []
    while snail_map:
        # Traverse top row
        result.extend(snail_map.pop(0))
        # Traverse right column
        for row in snail_map:
            result.append(row.pop())
        # Traverse bottom row in reverse
        if snail_map:
            result.extend(snail_map.pop()[::-1])
        # Traverse left column in reverse
        for row in snail_map[::-1]:
            result.append(row.pop(0))
    return result
