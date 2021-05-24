class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

        result = []

        while columnNumber > 0:
            result.append(capitals[(columnNumber - 1) % 26])
            columnNumber = columnNumber // 26

        result.reverse()
        return ''.join(result)