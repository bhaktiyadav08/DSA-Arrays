nums=[1,-1,0]
k=0
def subarraySum(nums,k):
    d={0:1}
    prefix=0
    count=0
    for i in range(len(nums)):
        prefix+=nums[i]
        if (prefix-k) in d:
            count+=d[prefix-k]
        d[prefix]=d.get(prefix,0)+1
    return count
print(subarraySum(nums,k))

            



                
                    

