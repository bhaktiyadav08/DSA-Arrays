nums=[-1,-2,5,4]
def maxProduct(nums):
    n=len(nums)
    nums.sort()
    res1=nums[n-1]*nums[n-2]*nums[n-3]
    res2=nums[0]*nums[1]*nums[n-1]
    return max(res1,res2)
print(maxProduct(nums))
