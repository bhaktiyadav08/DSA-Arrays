nums=[3,4,7,12,15]
target=13
def searchInsert(nums,target):
    n=len(nums)
    left, right = 0, n-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left
print(searchInsert(nums,target))
     
    
