class Solution(object):
    def isAnagram(self, s, t):
        d1={}
        if len(s)!=len(t):
            return False
        for char in s:
            d1[char]=d1.get(char,0)+1
        for char in t:
            if char not in d1:
                return False
            d1[char]-=1
            if d1[char]<0:
                return False
        return True
        




        