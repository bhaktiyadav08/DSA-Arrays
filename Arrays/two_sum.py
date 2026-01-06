arr=[4,7,5,3,9]
target=9
def two_sum(arr,target):
    n=len(arr)
    d={}
    for i,j in enumerate(arr):
        curr=target-i
        if curr in d:
            return (d[curr],j)
        d[i]=j

print(two_sum(arr,target))