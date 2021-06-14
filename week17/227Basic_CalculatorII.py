class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        sign = '+'
        num = 0

        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)

            if (not c.isdigit() and not c == ' ') or i == len(s) - 1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    if stack:
                        tmp = stack.pop()
                        stack.append(tmp * num)
                else:
                    if stack:
                        tmp = stack.pop()
                        stack.append(int(tmp / num))
                num = 0
                sign = c
        return sum(stack)
