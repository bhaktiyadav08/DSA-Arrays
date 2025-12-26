rows=[set() for _ in range (9)]
cols=[set() for _ in range (9)]
boxes=[set() for _ in range (9)]
board=[]
val=board[rows][cols]
def isSafe(board,rows,cols):
       for i in range(9):
            for j in range(9):
                val = board[i][j]
                
                if val == '.':
                    continue
                
                
                if val in rows[i]:
                    return False
                rows[i].add(val)
                
                # check column
                if val in cols[j]:
                    return False
                cols[j].add(val)
                
                # check 3x3 box
                box_index = (i // 3) * 3 + (j // 3)
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)
        
        return True
             
def sudokuSolver(board,rows,cols):
    if(rows==9):
        return True
    nxtrow=rows
    nxtcol=cols+1
    if(rows==9):
        rows=rows+1
        cols=0
    if(val!="."):
        return sudokuSolver(board,nxtrow,nxtcol)
    for digit in range (1,10):
        if (isSafe(board,rows,cols,digit)):
            board[rows][cols]=digit
            if (sudokuSolver(board)):
                return True
            board[rows][cols]="."
        return false
    
            
    




