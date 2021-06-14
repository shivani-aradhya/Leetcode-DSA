class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}

        for i in s:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1

        for i in t:
            if i not in d1:
                return False
            else:
                d1[i] -= 1
        """Values of all characters must be zero for being anagram"""
        for i in d1.values():
            if i != 0:
                return False
        return True
