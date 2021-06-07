class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()   #Keeps track of all squares

        while n not in visit:

            if n == 1:
                return True
            visit.add(n)
            n = self.square(n)

        return False
    """HELPER FUCTION TO SUM SQUARE OF NUMBER"""
    def square(self, n):

        sq = 0
        for i in str(n):
            sq += int(i) ** 2
        return sq
