class Solution(object):
    def maxMatrixSum(self, matrix):
        total = 0
        negCount = 0
        minAbs = float('inf')

        for row in matrix:
            for val in row:
                if val < 0:
                    negCount += 1
                absVal = abs(val)
                total += absVal
                minAbs = min(minAbs, absVal)

        if negCount % 2 == 0:
            return total
        else:
            return total - 2 * minAbs
