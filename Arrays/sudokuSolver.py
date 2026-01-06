board=[["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
def solveSudoku(board):
    def isSafe(r,c,num):
        for i in range(9):
         if board[r][i]==num:
            return False
        
        for i in range(9):
         if board[i][c]==num:
            return False
        startRow=(r//3)*3
        startCol=(c//3)*3
        for i in range(startRow,startRow+3):
         for j in range(startCol,startCol+3):
            if board[i][j]==num:
                return False
        return True
    def solve():
          for r in range(9):
             for c in range(9):
                if board[r][c]==".":
                   for num in "123456789":
                      if isSafe(r,c,num):
                         board[r][c]=num
                         if solve():
                            return True
                         board[r][c]="."
                   return False
          return True
    solve()
solveSudoku(board)
for row in board:
    print(row)

       


    

        

    