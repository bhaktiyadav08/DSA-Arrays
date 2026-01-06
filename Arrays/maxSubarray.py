nums=[-2,1,-3,4,-1,2,1,-5,4]
def maxSubarray(nums):
    n=len(nums)
    sum=nums[0]
    max=nums[0]
    if n==1:
        return sum
    for i in range(1,n):
        if nums[i]>(sum+nums[i]):
            sum=nums[i]
        else:
            sum=sum+nums[i]
        if sum>max:
            max=sum
    return max
print(maxSubarray(nums))