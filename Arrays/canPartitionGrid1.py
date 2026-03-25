def canPartitionGrid1(grid):
    rows = [sum(row) for row in grid]
    cols = [sum(col) for col in zip(*grid)]

    # 🔹 Check row-wise partition
    total = sum(rows)
    curr = 0
    for r in rows[:-1]:   # leave last (need 2 parts)
        curr += r
        if curr == total - curr:
            return True

    # 🔹 Check column-wise partition
    total = sum(cols)
    curr = 0
    for c in cols[:-1]:   # leave last
        curr += c
        if curr == total - curr:
            return True

    return False


# test
grid = [[100000,100000,92687]]
print(canPartitionGrid1(grid))