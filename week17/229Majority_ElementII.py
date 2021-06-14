class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        l = []
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        for num in d.keys():
            if d[num] > (len(nums) // 3):
                l.append(num)

        return (l)