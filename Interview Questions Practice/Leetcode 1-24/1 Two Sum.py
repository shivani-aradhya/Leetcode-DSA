class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[j] == target - nums[i]:
                    return i,j


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in d.keys() and i != d[rem]:
                return i, d[rem]

#SINGLE PASS
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining not in d:
                d[nums[i]] = i
            else:
                return d[remaining], i