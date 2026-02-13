def transformedArray(nums):
        n = len(nums)
        return [nums[((i + nums[i]) % n + n) % n] for i in range(n)]
print(transformedArray([1,-1,7,4]))
