matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
n=len(matrix[0])
def spiralMatrix2(matrix):
    left, right = 0, len(matrix[0])-1
    top , bottom = 0 , len(matrix)-1
    result=[]
    
    while top<=bottom and left<=right:
        for col in range(top,right+1):
         result.append(matrix[top][col])
        top+=1
    
        for row in range (top,bottom+1):
          result.append(matrix[row][right])
        right-=1
        if left<=right:
         for col in range (right,left-1,-1):
           result.append(matrix[bottom][col])
         bottom-=1
        if top<=bottom:
          for row in range (bottom,top-1,-1):
            result.append(matrix[row][left])
          left+=1
    return result
print(spiralMatrix2(matrix))
        