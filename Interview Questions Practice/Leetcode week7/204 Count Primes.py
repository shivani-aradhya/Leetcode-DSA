class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 2:
            return 0

        result = [True] * n
        result[0] = result[1] = False
        i = 2

        while i * i < n:
            if result[i] is True:
                for j in range(i * i, n, i):
                    result[j] = False
            i += 1

        return sum(result)