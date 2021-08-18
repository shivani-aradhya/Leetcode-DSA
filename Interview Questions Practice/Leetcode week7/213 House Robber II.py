class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return nums
        """ When arr=3 then only one house can be robbed"""
        if len(nums) <= 3:
            return max(nums)

        p1 = self.helper(nums[:len(nums) - 1])
        p2 = self.helper(nums[1:])

        return max(p1, p2)

    def helper(self, dp):
        dp[1] = max(dp[0], dp[1])

        for i in range(2, len(dp)):
            dp[i] = max(dp[i] + dp[i - 2], dp[i - 1])

        return dp[-1]
