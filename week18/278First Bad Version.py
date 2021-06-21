class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

#BINARY SEARCH O(LOGN)

"""BRUTE FORCE"""

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        for i in range(1, n):
            if isBadVersion(i):
                return i



