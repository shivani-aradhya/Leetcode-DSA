class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()   

        while n not in visit:

            if n == 1:
                return True
            visit.add(n)
            n = self.square(n)

        return False

    def square(self, n):

        sq = 0
        for i in str(n):
            sq += int(i) ** 2
        return sq