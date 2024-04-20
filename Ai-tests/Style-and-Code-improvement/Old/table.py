"""
Table
"""

def table(n,m):
    table = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        table[i][0] = 1
    for j in range(m):
        table[0][j] = 1
    def fill_table(i, j):
        if i < n and j < m:
            if table[i][j] == 0:
                table[i][j] = fill_table(i - 1, j) + fill_table(i, j - 1)
            return table[i][j]
        return 0
    fill_table(n - 1, m - 1)
    return table
