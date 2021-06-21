class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        """DYNAMIC PROGRAMING"""

        dp = [1] * len(nums)
        # Longest Subsequence till that index

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
