class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        current = 0
        maxReach = 0
        # LAST INDEX AVOIDED SINCE WE HAVE ALREADY REACHED THERE
        for i in range(len(nums) - 1):
            maxReach = max(maxReach, i + nums[i])
            if i == current:
                current = maxReach
                jump += 1

        return jump
