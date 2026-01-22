class Solution:
    def minOperations(self, nums):
        operations = 0
        
        # Helper function to check non-decreasing
        def is_non_decreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True
        
        while not is_non_decreasing(nums):
            # find the leftmost adjacent pair with minimum sum
            min_sum = float('inf')
            idx = 0
            for i in range(len(nums)-1):
                if nums[i] + nums[i+1] < min_sum:
                    min_sum = nums[i] + nums[i+1]
                    idx = i
            # merge the pair
            nums[idx] = nums[idx] + nums[idx+1]
            nums.pop(idx+1)
            operations += 1
        
        return operations
