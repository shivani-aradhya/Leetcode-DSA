class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        i = 0
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,"CD": 400, "D": 500, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
                 "CM": 900, "M": 1000}
        while i < len(s):
            if i < len(s) - 1 and s[i:i + 2] in roman:
                value += roman[s[i:i + 2]]
                i += 2
            else:
                value += roman[s[i]]
                i += 1

        return value