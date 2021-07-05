class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        l1 = len(num1)
        l2 = len(num2)
        res = [0] * (l1 + l2)
        i = l2 - 1
        pf = 0

        while i >= 0:
            ival = ord(num2[i]) - ord('0')
            j = l1 - 1
            carry = 0
            k = len(res) - 1 - pf
            while j >= 0 or carry != 0:
                if j >= 0:
                    jval = ord(num1[j]) - ord('0')
                else:
                    jval = 0

                prod = (ival * jval) + carry + res[k]
                res[k] = prod % 10
                carry = prod // 10
                j -= 1
                k -= 1
            pf += 1
            i -= 1

        str1 = ""
        flag = False

        str1 = ""
        for i in res:
            if i == 0 and not flag:
                continue
            else:
                str1 += chr(i + ord('0'))
                flag = True
        return str1

