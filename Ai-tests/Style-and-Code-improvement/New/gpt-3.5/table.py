"""
Table gtp-3.5
"""


def table(n, m):
    table = [[1] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            table[i][j] = table[i - 1][j] + table[i][j - 1]

    return table
