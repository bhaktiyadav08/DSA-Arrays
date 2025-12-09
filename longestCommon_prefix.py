strs=['flower','flow','float','flesh']
def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix=""
    first=strs[0]
    for i in range(len(first)):
        char=first[i]
        for s in strs:
            if i>len(s) or s[i]!=char:
             return prefix
        prefix+=char
print(longestCommonPrefix(strs))          