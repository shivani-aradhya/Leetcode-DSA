class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        rev = 0
        min = pow(-2, 31)
        max = (pow(2, 31) - 1)
        if x < 0:
            sign = -1
            x *= -1

        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x = x // 10

        result = rev * sign
        if min < result < max:
            return result
        return 0
