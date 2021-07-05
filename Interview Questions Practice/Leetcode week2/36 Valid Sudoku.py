class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr != '.':
                    if ("Found in row" + str(i) + curr) in seen or ("Found in col" + str(j) + curr) in seen or (
                            "Found in box" + str(i // 3) + str(j // 3) + curr) in seen:
                        return False
                    seen.add("Found in row" + str(i) + curr)
                    seen.add("Found in col" + str(j) + curr)

                    seen.add("Found in box" + str(i // 3) + str(j // 3) + curr)

        return True