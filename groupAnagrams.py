words=["eat","tea","tan","ate","nat","bat"]
def getHash(word):
    freq=[0]*26
    for ch in word:
        index=ord(ch)-ord('a')
        freq[index]+=1
    key=""
    for count in freq:
        key+=str(count)+"$"
    return key
def groupAnagram(words):
    result=[]
    hashmap={}
    for word in words:
        key=getHash(word)
        if key not in hashmap:
            hashmap[key]=len(result)
            result.append([])
        result[hashmap[key]].append(word)
        
    return result
print(groupAnagram(words))


