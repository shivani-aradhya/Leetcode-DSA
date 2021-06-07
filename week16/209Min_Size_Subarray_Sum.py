class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        """BRUTE FORCE APPROACH"""
        ans = float('inf')
        sum = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum = 0
                for k in range(i, j + 1):
                    sum += nums[k]

                if sum >= target:
                    ans = min(ans, j - i + 1)
                    break

        if ans == float('inf'):
            return 0
        else:
            return ans

"""OPTIMIZED CODE"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        ans = float('inf')
        i = 0
        j = 0
        sum = 0
        while i < len(nums):
            sum += nums[i]
            while sum >= target:
                ans = min(ans, i + 1 - j)
                sum -= nums[j]
                j += 1
            i += 1

        if ans == float('inf'):
            return 0
        return ans