class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):

                if numbers[i] + numbers[j] == target:
                    res.append(i + 1)
                    res.append(j + 1)

        return res
