class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        w1 = abs(ax2 - ax1)
        h1 = abs(ay2 - ay1)
        w2 = abs(bx2 - bx1)
        h2 = abs(by2 - by1)

        # Boundary regions
        right = min(ax2, bx2)
        left = max(ax1, bx1)

        top = min(ay2, by2)
        bottom = max(ay1, by1)
        area = (w1 * h1) + (w2 * h2)

        # width = max(right- left, 0)
        # height = max(top- bottom, 0)
        # Then can skip condition and direct compute

        if left < right and top > bottom:
            overlap = (right - left) * (top - bottom)
            return area - overlap
        else:
            return area