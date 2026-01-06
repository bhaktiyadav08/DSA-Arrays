nums=[4,7,3,1,4]
val=4

def removeElement(nums,val):
    n=len(nums)
    pos=0
    for i in range(0,n):
        if nums[i]==val:
            continue
        else:
           nums[pos]=nums[i]
           pos+=1
    return (pos)
print(removeElement(nums,val))