class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftmax = 0
        rightmax = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftmax:
                    leftmax = height[left]
                else:
                    water += (leftmax - height[left])
                left += 1
            else:
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    water += (rightmax - height[right])
                right -= 1

        return water

"""BRUTE FORCE"""


class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0
        for i in range(len(height)):
            leftmax = 0
            rightmax = 0
            for j in range(0, i + 1):
                leftmax = max(leftmax, height[j])
            for j in range(i, len(height)):
                rightmax = max(rightmax, height[j])
            water += min(leftmax, rightmax) - height[i]

        return water