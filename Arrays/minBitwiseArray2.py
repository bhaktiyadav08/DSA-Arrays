class Solution:
    def minBitwiseArray(self, nums):
        ans = []
        for p in nums:
            if p == 2:
                ans.append(-1)
            else:
                # Find position of first 0 bit from LSB
                bit = 0
                while (1 << bit) <= p:
                    if (p & (1 << bit)) == 0:
                        break
                    bit += 1
                # Minimal x
                x = p - (1 << (bit - 1))
                ans.append(x)
        return ans

# Test
nums = [2, 3, 5, 7]
print(Solution().minBitwiseArray(nums))  # Output: [-1, 1, 4, 3]
