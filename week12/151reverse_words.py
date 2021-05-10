class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()       #splitting
        left,right = 0,len(word)-1      #Taking two pointers
        while left < right:
            word[left],word[right] = word[right],word[left]    #swap
            left += 1
            right -= 1
        return ' '.join(word)