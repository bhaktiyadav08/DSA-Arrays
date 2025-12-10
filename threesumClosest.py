nums=[4,7,3,2,9]
target=10
def threesumClosest(nums):
   n=len(nums)
   nums.sort()
   closest=nums[0]+nums[1]+nums[2]
   for i in range(n-2):
        if i>0 and nums[i-1]==nums[i]:
            continue
        j,k=i+1,n-1
        while j<k:
            closest1=nums[i]+nums[j]+nums[k]
            if abs(closest1-target)<abs(closest-target):
                closest=closest1
                    
            if closest1<target:
                j+=1
            elif closest1>target:
                k-=1
            else:
                return target       
   return closest           
print(threesumClosest(nums))