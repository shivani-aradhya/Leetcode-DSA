class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1:
            return s

        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        res = ""
        for i in range(len(s)):
            # ODD CASE
            tmp = helper(i, i)
            if len(tmp) > len(res):
                res = tmp
            # EVEN CASE
            tmp1 = helper(i, i + 1)
            if len(tmp1) > len(res):
                res = tmp1

        return res
