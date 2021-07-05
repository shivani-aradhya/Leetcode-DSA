class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        if divisor == 1:
            return dividend

        negatives = 0
        if dividend < 0:
            negatives += 1
            dividend = - dividend
        if divisor < 0:
            negatives += 1
            divisor = -divisor
        q = 0
        while dividend - divisor >= 0:
            q += 1
            dividend = dividend - divisor

        return q if negatives != 1 else -q