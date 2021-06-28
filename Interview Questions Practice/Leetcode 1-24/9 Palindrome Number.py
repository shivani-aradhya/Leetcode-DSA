class Solution:
    def isPalindrome(self, x: int) -> bool:
        # REVERSING HALF INTEGER DIGITS

        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False

        reverse = 0
        while x > reverse:
            reverse = x % 10 + reverse * 10
            x = x // 10

        if x == reverse or x == (reverse // 10):
            return True
        return False

"""Slow Intuitive Approach"""
def isPalindrome(self, x: int) -> bool:
	if x<0:
		return False

	inputNum = x
	newNum = 0
	while x>0:
		newNum = newNum * 10 + x%10
		x = x//10
	return newNum == inputNum