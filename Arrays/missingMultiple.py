class Solution(object):
    def missingMultiple(self, nums, k):
        d={}
        for num in nums:
            if num%k==0:
                d[num]=d.get(num,0)+1
        sum=k
        i=1
        while sum in d:
            sum=k*i
            i+=1
        return sum 

        