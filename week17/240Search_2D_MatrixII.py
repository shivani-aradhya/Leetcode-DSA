class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False

"""OPTIMIZED"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        #START FROM BOTTOM-LEFT CORNER
        c =0
        r = row-1
        while r>=0 and c< col:
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                c+=1
            else:
                r-=1
        return False

"""EDGE CASE IS WHEN ROW =0 WHEN THERE IS ONLY ONE ELEMENT IN MATRIX"""
"""o(m+n) complexity"""