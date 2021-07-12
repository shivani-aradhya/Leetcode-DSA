class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        """BINARY SEARCH"""
        left = 2
        right = x // 2

        while left <= right:
            mid = (left + right) // 2
            mid_sq = mid * mid

            if mid_sq < x:
                left = mid + 1
            elif mid_sq > x:
                right = mid - 1
            else:
                return mid

        return right