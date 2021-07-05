class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        if 1 not in nums:
            return 1
        # CLEANING UP
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = len(nums) + 1

        # MARKING VALUES
        for num in nums:
            num = abs(num)
            if num <= len(nums) and nums[num - 1] >= 0:
                nums[num - 1] *= -1

        #FINAL SOLUTION AT FIRST INDEX VALUE WHICH IS POSITIVE
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1



"""NORMAL SOLUTION"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)+2):
            if i not in nums:
                return i
