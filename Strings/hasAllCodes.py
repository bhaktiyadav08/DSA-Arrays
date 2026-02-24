s='0110'
k=2
def hasAllCodes(s,k):
    seen=set()
    for i in range (len(s)-k+1):
        substring=s[i:i+k]
        seen.add(substring)
    if len(seen)==2**k:
        return True
    else:
        return False
print(hasAllCodes(s,k))

