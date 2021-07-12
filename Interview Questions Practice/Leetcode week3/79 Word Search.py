class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0] and self.search(board, x, y, 0, word):
                    return True
        return False

    def search(self, board, x, y, indx, word):
        if indx == len(word):
            return True

        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[indx]:
            return False

        temp = board[x][y]
        board[x][y] = ""
        found = self.search(board, x + 1, y, indx + 1, word) or self.search(board, x - 1, y, indx + 1,
                                                                            word) or self.search(board, x, y + 1,
                                                                                                 indx + 1,
                                                                                                 word) or self.search(
            board, x, y - 1, indx + 1, word)
        board[x][y] = temp

        return found