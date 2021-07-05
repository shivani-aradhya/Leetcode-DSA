class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        res = [-1, -1]

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                res[0] = mid
                # Look for first index of target in left array
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                res[1] = mid
                # Look for last index of target in right subpart of array
                left = mid + 1

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return res