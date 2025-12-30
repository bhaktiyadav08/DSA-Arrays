nums=[1,2,3]
result=[]
path=[]
nums.sort()
i=0
def subset(i):
    if i==len(nums):
        result.append(path.copy())
        return
    path.append(nums[i])
    subset(i+1)
    path.pop()
    while  i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
    subset(i+1)
subset(0)
print(result)

