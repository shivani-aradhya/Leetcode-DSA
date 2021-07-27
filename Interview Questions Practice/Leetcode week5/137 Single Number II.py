class Solution(object):
    def singleNumber(self, nums):

        if nums is None:
            return

        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for key in count:
            if count[key] == 1:
                return key