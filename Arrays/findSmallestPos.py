nums=[3,2,1,7,11,2]
def smallestPos(nums):
    n=len(nums)
    for i in range (0,n):
        while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
            correct_index=nums[i]-1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
    for i in range (0,n):
        if nums[i]!=i+1:
            return i+1

    return n+1
print(smallestPos(nums))