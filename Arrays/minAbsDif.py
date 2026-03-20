matrix=[[1,8],[3,-2]]
k=2
grid=[]
def minAbsDiff(matrix,k):
    res=[]
    n=len(matrix)
    m=len(matrix[0])
    for i in range(n-k):
        for j in range (m-k):
            for i1 in range(i,i+k-1):
                for j1 in range(j,j+k-1): 
                  grid.apppend(matrix[i1][j1])
            grid.sort()
            for t in range(1,len(grid)):
             curr=grid[t]-grid[t-1]
             if curr<minDiff:
              minDiff=curr
              res.append(minDiff)
    return min(res)


