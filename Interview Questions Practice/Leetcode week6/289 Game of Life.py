class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        rows = len(board)
        columns = len(board[0])
        new = [[board[row][col] for col in range(columns)] for row in range(rows)]

        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        for row in range(rows):
            for col in range(columns):
                live = 0
                for i in neighbors:
                    r = row + i[0]
                    c = col + i[1]

                    if (0 <= r < rows) and (0 <= c < columns) and new[r][c] == 1:
                        live += 1
                if new[row][col] == 1 and (live < 2 or live > 3):
                    board[row][col] = 0

                if new[row][col] == 0 and (live == 3):
                    board[row][col] = 1