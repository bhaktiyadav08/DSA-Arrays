class Solution(object):
    def minWindow(self, s, t):
        if len(t)>len(s):
            return ""
        d1={}
        k=len(t)
        for ch in t:
            d1[ch]=d1.get(ch,0)+1
        left=0
        d2={}
        have=0
        need=len(d1)
        min_len=float('inf')
        for right in range(len(s)):
            if s[right] in t:
                d2[s[right]]=d2.get(s[right],0)+1
                if d2[s[right]]==d1[s[right]]:
                    have+=1
            while have==need:
                curr_len=right-left+1
                if curr_len<min_len:
                    min_len=curr_len
                    start=left
                if s[left] in d1:
                    d2[s[left]]-=1
                    if d2[s[left]]<d1[s[left]]:
                        have-=1
                left+=1
        if min_len==float('inf'):
            return ""
        else:
            return s[start:start+min_len]
                    
                

            