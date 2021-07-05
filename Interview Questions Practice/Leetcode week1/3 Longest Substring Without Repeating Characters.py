class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        # Recording index of characters
        seen = {}
        i = 0
        res = 0
        for j in range(len(s)):
            if s[j] in seen:
                i = max(i, (seen[s[j]] + 1))

            res = max(res, j - i + 1)
            seen[s[j]] = j
        return res


"""BRUTE FORCE"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.check(s, i, j):
                    res = max(res, j - i + 1)

        return res

    def check(self, s, start, end):
        values = dict()
        for i in range(start, end + 1):
            if s[i] not in values:
                values[s[i]] = 1
            else:
                return False
        return True