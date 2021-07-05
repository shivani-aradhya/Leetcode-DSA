class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        l = len(nums)
        maxReach = 0
        for i in range(l):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
        return True