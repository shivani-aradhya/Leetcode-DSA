class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            a = pattern[i]
            b = words[i]

            if a not in d:
                if b in d.values():
                    return False
                d[a] = b
            else:
                if d[a] != b:
                    return False

        return True
