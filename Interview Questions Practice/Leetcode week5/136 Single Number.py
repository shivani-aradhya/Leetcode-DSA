class Solution(object):
    def singleNumber(self, nums):

        lst = []

        if not nums:
            return

        for i in nums:
            if i not in lst:
                lst.append(i)
            else:
                lst.remove(i)

        return lst.pop()