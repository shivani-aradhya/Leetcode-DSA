class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1]
        pointers = [0 for i in range(len(primes))]

        for i in range(1, n):
            p = [dp[e] * primes[j] for j, e in enumerate(pointers)]
            min_i = min(p)
            dp.append(min_i)
            for j, e in enumerate(p):
                if e == min_i: pointers[j] += 1

        return dp[-1]