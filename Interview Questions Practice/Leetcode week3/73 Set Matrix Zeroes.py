class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])

        row = [1] * r
        col = [1] * c

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0

        for i in range(r):
            if row[i] == 0:
                matrix[i] = [0] * c

        for i in range(c):
            if col[i] == 0:
                for j in range(r):
                    matrix[j][i] = 0
