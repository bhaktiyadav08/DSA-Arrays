arr=[1,-1,4,0,2]
result=[]
def threesum(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (arr[i]+arr[j]+arr[k])==0:
                    triplet=sorted([arr[i],arr[j],arr[k]])
                    if triplet not in result:
                        result.append(triplet)
    return result
print(threesum(arr))

