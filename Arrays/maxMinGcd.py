import math
class Solution:
    def findGCD(self, nums):
        min_num=min(nums)
        max_num=max(nums)
        return math.gcd(max_num,min_num)
        