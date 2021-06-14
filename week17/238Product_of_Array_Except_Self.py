"""O(N) TIME AND SPACE COMPLEXITY"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        left = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        right = [1]
        for i in range(len(nums) - 1, 0, -1):
            right.append(right[-1] * nums[i])
        right = right[::-1]

        output = [None] * len(nums)
        for i in range(len(nums)):
            output[i] = left[i] * right[i]

        return output

"""OPTIMIZED CODE"""
"""O(N) TIME AND O(1 )SPACE COMPLEXITY"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        output = [1]  # Right
        for i in range(len(nums) - 1, 0, -1):
            output.append(output[-1] * nums[i])
        output = output[::-1]

        left = 1
        for i in range(len(nums)):
            output[i] = left * output[i]
            left *= nums[i]

        return output