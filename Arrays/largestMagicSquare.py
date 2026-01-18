class Solution:
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])

        # Prefix sums
        rowSum = [[0] * (n + 1) for _ in range(m)]
        colSum = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                rowSum[i][j + 1] = rowSum[i][j] + grid[i][j]
                colSum[i + 1][j] = colSum[i][j] + grid[i][j]

        def getRow(i, l, r):
            return rowSum[i][r] - rowSum[i][l]

        def getCol(j, t, b):
            return colSum[b][j] - colSum[t][j]

        maxSize = min(m, n)

        for size in range(maxSize, 1, -1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    target = getRow(i, j, j + size)

                    ok = True
                    # Check rows
                    for r in range(i, i + size):
                        if getRow(r, j, j + size) != target:
                            ok = False
                            break

                    # Check columns
                    for c in range(j, j + size):
                        if getCol(c, i, i + size) != target:
                            ok = False
                            break

                    # Check diagonals
                    diag1 = sum(grid[i + k][j + k] for k in range(size))
                    diag2 = sum(grid[i + k][j + size - 1 - k] for k in range(size))

                    if diag1 != target or diag2 != target:
                        ok = False

                    if ok:
                        return size

        return 1
