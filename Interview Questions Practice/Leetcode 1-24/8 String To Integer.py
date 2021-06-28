class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        l = s.strip()
        max_int = pow(2, 31) - 1
        min_int = pow(-2, 31)
        sign = 1
        val = 0

        if l[0] == "-":
            sign = -1
        elif l[0] == "+":
            sign = 1
        elif not l[0].isdigit():
            return 0
        else:
            val = ord(l[0]) - ord("0")

        for i in range(1, len(l)):
            if l[i].isdigit():
                val = val * 10 + (ord(l[i]) - ord("0"))
            else:
                break
                
        val = sign * val

        if sign == 1:
            return min(max_int, val)
        if sign == -1:
            return max(min_int, val)