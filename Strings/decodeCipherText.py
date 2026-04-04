class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # Calculate the number of columns in the grid
        n = len(encodedText)
        cols = n // rows
        
        res = []
        # Iterate through each possible starting column for a diagonal
        for c in range(cols):
            # Traverse the diagonal starting from row 0, column c
            # The next element in the diagonal is (row + 1, col + 1)
            # In the 1D encodedText, this maps to: current_index + (cols + 1)
            for i in range(c, n, cols + 1):
                res.append(encodedText[i])
        
        # Join characters and remove trailing spaces as per problem requirements
        return "".join(res).rstrip()
