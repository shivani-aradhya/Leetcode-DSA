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