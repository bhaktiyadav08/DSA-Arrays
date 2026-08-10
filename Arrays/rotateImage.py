matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
def rotateImage(matrix):
    #res=[[0 for _ in range(len(matrix))]for _ in range(len(matrix))]
    for col in range(len(matrix)):
        for row in range(col,len(matrix)):
            matrix[row][col],matrix[col][row]=matrix[col][row],matrix[row][col]
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix
print(rotateImage(matrix))
