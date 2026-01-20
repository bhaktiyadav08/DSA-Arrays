class Solution:
    def minBitwiseArray(self, nums):
        ans = []

        for n in nums:
            found = False
            for x in range(n):
                if (x | (x + 1)) == n:
                    ans.append(x)
                    found = True
                    break
            if not found:
                ans.append(-1)

        return ans
