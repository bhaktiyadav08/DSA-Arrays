class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        d1={}
        k=len(s1)
        for ch in s1:
            d1[ch]=d1.get(ch,0)+1
        d2={}
        for i in range(k):
            d2[s2[i]]=d2.get(s2[i],0)+1
        left=0
        right=k-1
        if d1==d2:
            return True
        while right<len(s2)-1:
            d2[s2[left]]-=1
            if d2[s2[left]]==0:
                del d2[s2[left]]
            left+=1
            right+=1
            d2[s2[right]]=d2.get(s2[right],0)+1
            if d1==d2:
                return True
          
        return False
