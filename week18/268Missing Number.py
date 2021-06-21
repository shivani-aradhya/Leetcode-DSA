class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        large = max(nums)
        if 0 not

        for i in range(0, large + 1):
            if i not in nums:
                return i

        return large + 1

"""BETTER SOLUTION"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """SUM OF FIRST N NATURAL NUMBERS"""
        if 0 not in nums:
            return 0
        expected = len(nums) * (len(nums) + 1) // 2

        sum = 0
        for i in range(len(nums)):
            sum += nums[i]

        return (expected - sum)