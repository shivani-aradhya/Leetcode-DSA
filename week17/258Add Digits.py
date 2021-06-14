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

"""OPTIMIZED 0(1) CODE BASED ON DIGITAL ROOT
THAT A NUMBER CAN BE EXPRESSED IN MULTPLES OF 10 WHICH CAN FURTHER BE EXPRESSED IN 9
num = 9k + a """

class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        elif num%9 ==0:
            return 9
        else:
            return num%9