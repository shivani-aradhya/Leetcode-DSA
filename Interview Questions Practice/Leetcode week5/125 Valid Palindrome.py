class Solution:
    def isPalindrome(self, str):

        res =""
        for i in str:
            if i.isalnum():
                res = res+ i.lower()

        n = len(s)
        left= 0
        right= n-1

        while left<right:
             if res[left]!=res[right]:
                 return False

             left+=1
             right-=1

        return True