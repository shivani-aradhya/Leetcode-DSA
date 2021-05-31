"""Number of trailing zeroes dictated by number of 5 as number of 2s occur more frequently"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n != 0:
            n = n // 5
            count += n
        return count