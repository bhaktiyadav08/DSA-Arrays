class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        maxArea = 0

        for row in matrix:
            # Step 1: Build histogram heights
            for c in range(cols):
                if row[c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0

            # Step 2: Find largest rectangle in histogram
            stack = []
            for i in range(cols + 1):
                curr = heights[i] if i < cols else 0

                while stack and curr < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    maxArea = max(maxArea, h * w)

                stack.append(i)

        return maxArea
