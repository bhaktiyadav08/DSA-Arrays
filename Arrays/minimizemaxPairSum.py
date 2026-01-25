class Solution:
    def minPairSum(self, nums: list):
        # Sort the array
        nums.sort()
        
        # Initialize variables
        max_sum = 0
        left = 0
        right = len(nums) - 1
        
        # Pair elements from both ends
        while left < right:
            current_sum = nums[left] + nums[right]
            max_sum = max(max_sum, current_sum)
            left += 1
            right -= 1
        
        return max_sum