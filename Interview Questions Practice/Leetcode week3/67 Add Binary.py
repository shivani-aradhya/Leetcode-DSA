class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""
        a = list(a)
        b = list(b)
        while a or b or carry == 1:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry % 2)
            carry = carry // 2

        return result[::-1]