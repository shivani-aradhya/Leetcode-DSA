class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 1:
            return matrix

        def transpose(matrix):

            n = len(matrix)
            for i in range(n):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reverseRow(matrix):
            n = len(matrix)
            for i in range(n):
                left = 0
                right = n - 1
                while left < right:
                    matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                    left += 1
                    right -= 1

        transpose(matrix)
        reverseRow(matrix)
