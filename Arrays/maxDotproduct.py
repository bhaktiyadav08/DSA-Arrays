class Solution:
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        memo = {}

        def dp(i, j):
            if i == n or j == m:
                return float('-inf')

            if (i, j) in memo:
                return memo[(i, j)]

            # Option 1: Take both nums1[i] and nums2[j]
            take = nums1[i] * nums2[j] + max(0, dp(i+1, j+1))

            # Option 2: Skip nums1[i]
            skip1 = dp(i+1, j)

            # Option 3: Skip nums2[j]
            skip2 = dp(i, j+1)

            memo[(i, j)] = max(take, skip1, skip2)
            return memo[(i, j)]

        return dp(0, 0)
