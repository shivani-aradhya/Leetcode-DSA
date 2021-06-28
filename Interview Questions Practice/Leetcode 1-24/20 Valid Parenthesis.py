class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {')': '(', '}': '{', ']': '['}

        stack = []

        for i in s:
            if i not in brackets.keys():
                stack.append(i)
            else:
                if stack:
                    if stack[-1] != brackets[i]:
                        return False
                    else:
                        stack.pop()

                else:
                    return False

        return len(stack) == 0
