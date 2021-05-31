class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for char in columnTitle:
            asciivalue = ord(char) - ord('A') + 1
            num = num * 26 + asciivalue

        return num