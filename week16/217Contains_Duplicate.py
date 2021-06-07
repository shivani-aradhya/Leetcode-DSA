"""TIME LIMIT EXCEEDED O(N2) APPROACH"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]== nums[j]:
                    return True
        return False

"""O(N) APPROACH"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen.keys():
                return True
            else:
                seen[num] = 1
        return False
