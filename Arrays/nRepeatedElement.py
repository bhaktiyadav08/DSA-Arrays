nums = [3,2,3,1,2,3]
def nRepeatedElement(nums):
    n=len(nums)
    pos={}
    for num in nums:
        pos[num]=pos.get(num,0)+1
        if pos[num]==n//2:
            return num
print(nRepeatedElement(nums))