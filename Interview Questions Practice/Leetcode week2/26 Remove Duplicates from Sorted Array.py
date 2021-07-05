class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1

        if len(nums) == 0:
            return 0

        while right < len(nums):
            while right < len(nums) and nums[left] == nums[right]:
                del nums[right]


            else:
                left += 1
                right += 1

        return len(nums)
