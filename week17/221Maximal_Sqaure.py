class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        if row == 1 and matrix[0] == 1:
            return 1
        if row == 1 and matrix[0] == 0:
            return 0

        dp = [[0] * (col + 1) for i in range(row + 1)]
        l = 0
        for i in range(1, row + 1):
            for j in range(1, col + 1):

                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    l = max(l, dp[i][j])
        return l * l
