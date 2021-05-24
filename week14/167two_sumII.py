"""O(n2) approach"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):

                if numbers[i] + numbers[j] == target:
                    res.append(i + 1)
                    res.append(j + 1)

        return res


"""OPTIMIZED APPROACH"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left + 1, right + 1]
