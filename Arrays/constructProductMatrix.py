grid=[[1,2],[3,4]]
def constructProductMatrix(grid):
    m=len(grid)
    n=len(grid[0])
    arr=[0]*(m*n)
    ans=[[0]*n for _ in range (m)]
    for i in range (m):
        for j in range (n):
            index=i*(n)+j
            arr[index]=grid[i][j]
    size=len(arr)
    prefix=[0]*size
    suffix=[0]*size
    suffix[size-1]=1
    prefix[0]=1
    for i in range (1,size):
        prefix[i]=prefix[i-1]*arr[i-1]%12345
    for i in range (size-2,-1,-1):
        suffix[i]=suffix[i+1]*arr[i+1]%12345
    for k in range (m):
        for l in range (n):
            idx=k*n+l
            ans[k][l]=(prefix[idx]*suffix[idx])%12345
    return ans
print(constructProductMatrix(grid))   
