class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        # FIRST FINDING ROW
        row = 0
        M = len(matrix)
        for r in range(M):
            if matrix[r][0] == target or matrix[r][-1] == target:
                return True
            elif matrix[r][0] < target < matrix[r][-1]:
                row = r
                break

        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False