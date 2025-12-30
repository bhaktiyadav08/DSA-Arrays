nums=[1,2,3]
result=[]
path=[]
i=0
def subset(i):
    if i==len(nums):
        result.append(path.copy())
        return
    path.append(nums[i])
    subset(i+1)
    path.pop()
    subset(i+1)

print(result)

