nums=[1,-1,0]
k=0
def subarraySum(nums,k):
    res=[]
    for i in range(len(nums)):
        if nums[i]==k:
            res.append([nums[i]])
        else:
            sum=nums[i]
            j=i
            while(sum!=k and j!=len(nums)):
                sum+=nums[j]
                j+=1
            if sum==k:
                res.append(nums[i:j])
    return res
print(subarraySum(nums,k))


                
                    

