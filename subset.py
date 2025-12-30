nums=[1,2,3]
result=[]
path=[]
i=0
def backtrack(i):
    if i==len(nums):
        result.append(path.copy())
        return
    path.append(nums[i])
    backtrack(i+1)
    path.pop()
    backtrack(i+1)
backtrack(0)
print(result)

