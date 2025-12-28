words=["eat","tea","tan","ate","nat","bat"]
MAX_CHAR = 26  # number of letters in the alphabet

def getHash(word):
    freq = [0] * MAX_CHAR  # initialize frequency array
    
    # Count frequency of each letter
    for ch in word:
        index = ord(ch) - ord('a')  # find position in alphabet
        freq[index] += 1
    
    # Convert frequency array to string with '$' separator
    key = ""
    for count in freq:
        key += str(count) + "$"
    
    return key
def groupAnagrams(words):
    result = []      # list to hold groups
    hashmap = {}     # key -> index in result list
    
    for word in words:
        key = getHash(word)   # get the fingerprint
        
        if key not in hashmap:
            # new group
            hashmap[key] = len(result)
            result.append([])
        
        # add word to its group
        result[hashmap[key]].append(word)
    
    return result
print(groupAnagrams(words))
