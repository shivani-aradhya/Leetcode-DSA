class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n>=0:
            if n==1:
                return True
            elif n%2==0:
                n=n/2
            else:
                return False