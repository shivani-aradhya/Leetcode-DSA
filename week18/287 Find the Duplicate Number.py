class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

        for i in d.keys():
            if d[i] > 1:
                return i