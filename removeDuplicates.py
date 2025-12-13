nums=[1,2,3,3,5,7]

def removeDuplicates(nums):
    if not nums:
        return 0
    n=len(nums)
    pos=0
    for i in range(1,n):
        if nums[pos]==nums[i]:
            continue
        else:
            pos+=1
            nums[pos]=nums[i]
            
    return (pos+1)
print(removeDuplicates(nums))