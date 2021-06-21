class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 0:
            return
        lst = []
        for a in range(32):
            for b in range(20):
                for c in range(14):
                    lst.append(2 ** a * 3 ** b * 5 ** c)

        lst.sort()
        return lst[n - 1]

"""OPTIMIZED APPROACH USING MULTIPLIERS LIST FOR 2, 3,5"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 0:
            return
        ugly = [1]
        # Three Pointers
        two = 0
        three = 0
        five = 0

        while len(ugly) < n:

            val2 = ugly[two] * 2               #Keeps track of last multiplier value in sorted fashion
            val3 = ugly[three] * 3
            val5 = ugly[five] * 5

            minimum = min(val2, val3, val5)
            ugly.append(minimum)

            if minimum == val2:
                two += 1
            if minimum == val3:
                three += 1
            if minimum == val5:
                five += 1

        return ugly[-1]
