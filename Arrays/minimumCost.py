nums=[10,3,1,1]
def minimumCost(nums):
  return nums[0]+ sum(sorted(nums[1:])[:2])
print(minimumCost(nums))

    