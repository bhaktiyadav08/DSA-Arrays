arr=[4,7,5,3,9]
target=9
def two_sum(arr,target):
    n=len(arr)
    d={}
    for i,j in enumerate(arr):
        curr=target-j
        if curr in d:
            return (d[curr],i)
        d[j]=i

print(two_sum(arr,target))