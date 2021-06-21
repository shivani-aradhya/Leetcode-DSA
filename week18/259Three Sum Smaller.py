"""BRUTE FORCE"""
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):

                    if nums[i] + nums[j] + nums[k] < target:
                        count += 1

        return count


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        if nums == [] or len(nums) < 3:
            return 0

        nums.sort()
        for i in range(len(nums) - 2):
            first = i + 1
            last = len(nums) - 1
            while first < last:
                if nums[i] + nums[first] + nums[last] < target:
                    count += last - first
                    first += 1

                else:
                    last -= 1

        return count



class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        if nums == [] or len(nums) < 3:
            return 0
        nums.sort()
        for i in range(len(nums) - 2):
            count += self.twoSum(nums, i + 1, target - nums[i])
        return count

    def twoSum(self, nums, start, target):
        sum = 0
        first = start
        last = len(nums) - 1
        while first < last:
            if nums[first] + nums[last] < target:
                sum += last - first
                first += 1

            else:
                last -= 1
        return sum