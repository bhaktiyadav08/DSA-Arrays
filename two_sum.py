arr=[4,7,5,3,9]
target=9
def two_sum(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return[i,j]
            
        
print(two_sum(arr,target))