class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):

                target1 = target - nums[i] - nums[j]
                low = j + 1
                high = len(nums) - 1

                while low < high:
                    total = nums[low] + nums[high]

                    if total > target1:
                        high -= 1
                    elif total < target1:
                        low += 1
                    else:
                        output.add((nums[i], nums[j], nums[low], nums[high]))
                        high -= 1

        return output