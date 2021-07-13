class Solution:
    def numTrees(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        count =0
        for i in range(1, n+1):
            #LEFT SUBTREE i-1
            #RIGHT SUBTREE n-i
            count += self.numTrees(i-1)* self.numTrees(n-i)
        return count