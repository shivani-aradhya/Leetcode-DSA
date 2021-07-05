class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return 0
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        output = []
        while left <= right and top <= bottom:
            # TOP ROW
            for i in range(left, right + 1):
                output.append(matrix[top][i])
            top += 1
            # RIGHT SIDE
            for i in range(top, bottom + 1):
                output.append(matrix[i][right])
            right -= 1

            if not (left <= right and top <= bottom):
                break

            # BOTTOM SIDE
            for i in range(right, left - 1, -1):
                output.append(matrix[bottom][i])
            bottom -= 1
            # LEFT SIDE
            for i in range(bottom, top - 1, -1):
                output.append(matrix[i][left])
            left += 1

        return output