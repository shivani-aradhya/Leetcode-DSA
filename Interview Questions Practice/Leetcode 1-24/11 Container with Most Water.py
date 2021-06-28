class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        if len(height) == 1 and height[0] == 0:
            return 0

        water = 0
        left = 0
        right = len(height) - 1
        while left < right:
            w = right - left
            h = min(height[right], height[left])

            water = max(water, w * h)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return water