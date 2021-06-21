class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        dict = {}
        for i in range(len(nums)):
            s = nums[i]
            if s not in dict:
                dict[s] = 1
            else:
                dict[s] -= 1

        lst = []
        for i in dict:
            if dict[i] == 1:
                lst.append(i)

        return lst