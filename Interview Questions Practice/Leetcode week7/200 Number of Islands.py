class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        lst = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

        for row, col in lst:
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == '1':
                self.dfs(grid, row, col)

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    islands += 1

        return islands