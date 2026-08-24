s = "AABABBA"
k=1
def charReplacement(s,k):
    l=0
    max_freq=0
    max_length=0
    d={}
    for r in range(len(s)):
        d[s[r]]=d.get(s[r],0)+1
        max_freq=max(d[s[r]],max_freq)
        if (r-l+1)-max_freq>k:
            d[s[l]]-=1
            l+=1
        max_length=max(r-l+1,max_length)
    return max_length
print(charReplacement(s,k))

