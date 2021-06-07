class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count1 = dict()
        count2 = dict()

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if c1 not in count1:
                count1[c1] = c2

            if c2 not in count2:
                count2[c2] = c1

            if count1[c1] != c2 or count2[c2] != c1:
                return False
        return True
