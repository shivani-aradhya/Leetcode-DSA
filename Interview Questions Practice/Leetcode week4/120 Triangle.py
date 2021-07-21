class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        result = [num for num in triangle[-1]]

        for row in range(len(triangle) - 1, -1, -1):
            for col in range(0, row + 1):
                result[col] = triangle[row][col] + min(result[col] + result[col + 1])

        return result[0]