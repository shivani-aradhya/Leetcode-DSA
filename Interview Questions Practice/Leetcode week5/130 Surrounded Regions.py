class Solution:
    def solve(self, board):
        if not board:
            return

        height= len(board)
        width= len(board[0])

        def mark(r,c):
            if 0<=r<=height and 0<=c<=width and board[r][c]=='0':
                board[r][c]=='S'
                mark(r-1,c)
                mark(r+1,c)
                mark(r,c-1)
                mark(r, c+1)

        #first row
        for r in [0,height-1]:
            for c in range(width):
                mark(r,c)

        for c in [0,width-1]:
            for r in range(height):
                mark(r,c)

        for r in range(height):
            for c in range(width):
                if board[r][c]=='S':
                    board[r][c]='0'
                elif board[r][c]=='0':
                    board[r][c] == 'X'
