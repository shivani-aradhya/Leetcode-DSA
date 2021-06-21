class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False

        p = [2, 3, 5]
        for i in p:
            while n % i == 0:
                n = n // i
        if n == 1:
            return True
        else:
            return False
