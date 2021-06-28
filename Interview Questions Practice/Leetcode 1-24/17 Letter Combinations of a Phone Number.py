class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        if not digits:
            return []

        output = [""]
        for digit in digits:
            tmp = []
            for i in mapping[digit]:
                for o in output:
                    tmp.append(o + i)
            output = tmp

        return output