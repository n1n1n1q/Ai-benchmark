def snail(snail_map):
    if snail_map == [[]]:
        return []

    result = []
    while snail_map:
        # add the first row to result
        result += snail_map.pop(0)
        if snail_map:
            # add the last column to result
            for row in snail_map:
                result.append(row.pop())
        if snail_map:
            # add the last row to result in reversed order
            result += snail_map.pop()[::-1]
        if snail_map:
            # add the first column to result in reversed order
            for row in snail_map[::-1]:
                result.append(row.pop(0))
    return result
