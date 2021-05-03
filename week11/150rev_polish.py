class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        """Declaring list of operators for transversal"""
        operator = ['+', '-', '*', '/', '%']

        for i in tokens:
            if i not in operator:
                stack.append(int(i))  # IF NUMBER

            else:
                first = stack.pop()
                second = stack.pop()

                if i == "+":
                    stack.append(second + first)
                elif i == "-":
                    stack.append(second - first)
                elif i == "*":
                    stack.append(second * first)
                elif i == "/":
                    stack.append(int(second / first))
                else:
                    stack.append(second % first)

            return stack[-1]           #Returning top element which is the result
