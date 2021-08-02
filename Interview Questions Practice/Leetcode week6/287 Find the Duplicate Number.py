class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        seen = {}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 1
            else:
                seen[nums[i]] += 1

        for i in seen.keys():
            if seen[i] > 1:
                return i