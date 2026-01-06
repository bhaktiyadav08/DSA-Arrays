def wordBreak(s, wordDict):
    wordSet = set(wordDict)   # O(1) lookup
    n = len(s)
    
    # dp[i] = True if s[0:i] can be segmented using dict
    dp = [False] * (n + 1)
    dp[0] = True   # empty string is valid

    for i in range(1, n + 1):
        for j in range(i):
            # if left part is valid and right part is a word
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break

    return dp[n]