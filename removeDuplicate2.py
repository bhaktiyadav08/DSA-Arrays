nums=[1,2,2,2,3,7,9]
def removeDuplicates2(nums):
    n=len(nums)
    if n<=2:
        return n
    i=2
    for j in range (2,n):
        if nums[j]!=nums[i-2]:
            nums[i]=nums[j]
            i+=1
    return i
print(removeDuplicates2(nums))