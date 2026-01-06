class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            # If all characters matched
            if i == len(word):
                return True
            
            # Out of bounds or mismatch
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False
            if board[r][c] != word[i]:
                return False
            
            # Mark this cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all 4 directions
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # Backtrack (restore cell)
            board[r][c] = temp

            return found

        # Try starting from every cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        
        return False
