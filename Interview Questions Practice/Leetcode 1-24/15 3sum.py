class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):

            if i == 0 or nums[i - 1] != nums[i]:
                low = i + 1
                high = len(nums) - 1
                target = 0 - nums[i]

                while low < high:
                    sum = nums[low] + nums[high]
                    if target > sum:
                        low += 1
                    elif target < sum:
                        high -= 1
                    else:
                        res.append([nums[i], nums[low], nums[high]])
                        low += 1
                        high -= 1
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1

        return res
