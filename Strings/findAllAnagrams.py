class Solution(object):
    def findAnagrams(self, s, p):
        if len(p)>len(s):
            return []
        k=len(p)
        res=[]
        d1={}
        for ch in p:
            d1[ch]=d1.get(ch,0)+1
        d2={}
        left=0
        right=k
        for i in range(k):
            d2[s[i]]=d2.get(s[i],0)+1
        if d1==d2:
            res.append(left)
        while right<len(s):
            d2[s[left]]-=1
            if d2[s[left]]==0:
                del d2[s[left]]
            left+=1
            d2[s[right]]=d2.get(s[right],0)+1
            if d1==d2:
                res.append(left)
            right+=1
        return res
       
        