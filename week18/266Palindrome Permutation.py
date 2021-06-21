class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        seen = set()
        for i in s:
            if i not in seen:
                seen.add(i)
            else:
                seen.remove(i)

        return len(seen) <= 1

"""DISTINCT ELEMENTS SHOULD NOT BE GREATER THAN 1
ODD NUMBER OF OCCURENCES SHOULD NOT BE MORE THAN 1 OF ANY CHARACTER IN STRING"""