class Solution:
    def addDigits(self, num: int) -> int:
        if not num:
            return 0

        if len(str(num)) == 1:
            return num

        res = 0
        while num > 0:
            res += num % 10
            num = num // 10

            if num == 0 and res > 9:
                num = res
                res = 0

        return res