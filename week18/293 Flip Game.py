class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        if len(currentState) < 2:
            return []
        valid = []

        for i in range(1, len(currentState)):
            s = currentState[i]
            s1 = currentState[i - 1]
            if s1 + s == "++":
                valid.append(currentState[:i - 1] + "--" + currentState[i + 1:])

        return valid