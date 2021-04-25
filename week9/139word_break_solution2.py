class Solution(object):
    def wordBreak(self, s, wordDict):

        dp = [True] + [False] * len(s)

        for index in range(1, len(s) + 1):
            for word in wordDict:

                if s[:index].endswith(word) and dp[index - len(word)] == True:
                    dp[index] = True
        return dp[-1]