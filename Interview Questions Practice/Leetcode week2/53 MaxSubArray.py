"""BRUTE FORCE"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxSum = float('-inf')
        for i in range(len(nums)):
            currentSum = 0
            for j in range(i, len(nums)):
                currentSum += nums[j]
                maxSum = max(maxSum, currentSum)

        return maxSum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        currentSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            maxSum = max(maxSum, currentSum)

        return maxSum