nums = [1,2,3,4,3]
def nextGreaterElementII(nums):
    n=len(nums)
    stack=[]
    res=[-1]*n
    for i in range(2*n):
        curr=i%n
        while stack and nums[curr]>nums[stack[-1]]:
            idx=stack.pop()
            res[idx]=nums[curr]
        stack.append(curr)        
    return res
print(nextGreaterElementII(nums))