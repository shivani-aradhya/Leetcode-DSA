class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        diff = float('inf')
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                low = i + 1
                high = len(nums) - 1
                while low < high:
                    value = nums[low] + nums[high] + nums[i]
                    if target == value:
                        return value

                    if abs(diff) > abs(target - value):
                        diff = target - value
                    if target > value:
                        low += 1
                    else:
                        high -= 1

        return target - diff
