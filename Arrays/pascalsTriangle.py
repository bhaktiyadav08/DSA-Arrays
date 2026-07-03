class Solution(object):
    def generate(self, numRows):
        n=numRows
        arr=[[0]*(i+1) for i in range(n)]

        for i in range(n):
            arr[i][0]=1
            arr[i][i] =1
            for j in range(1,i):
                arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
        return arr
        