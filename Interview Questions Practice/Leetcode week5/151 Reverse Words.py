class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        left,right = 0,len(word)-1
        while left < right:
            word[left],word[right] = word[right],word[left]    
            left += 1
            right -= 1
        return ' '.join(word)