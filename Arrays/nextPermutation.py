nums=[3,6,5,7,8,9]
def nextPermutation(nums):
    pivot=-1
    n=len(nums)
    for i in range(n-2,-1,-1):
        if nums[i]<nums[i+1]:
            pivot=i
            break
    if pivot==-1:
        start=0
        end=n-1
        while(start<end):
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
            return
    for i in range (n-1,pivot,-1):
        if nums[i]>nums[pivot]:
            nums[i], nums[pivot] = nums[pivot], nums[i]
            break
        
    start, end = pivot+1, n-1
    while start<end:
        nums[start], nums[end] = nums[end], nums[start]
        start+=1
        end-=1
    return nums
print(nextPermutation(nums))
