arr=[1,1,1,6,1,1,1]
def houseDiffColor(arr):
    n=len(arr)
    max_dist=0
    for i in range (n-1,-1,-1):
        if arr[i]!=arr[0]:
            max_dist=max(max_dist,i)
            break
    for j in range (n):
        if arr[i]!=arr[n-1]:
            max_dist=max(max_dist,(n-1)-i)
            break
    return max_dist
print(houseDiffColor(arr))


