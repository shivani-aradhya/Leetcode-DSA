from collections import deque


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        diff = float('inf')
        q = deque([root])
        closest = 0

        while q:
            node = q.popleft()
            if abs(node.val - target) < diff:
                diff = abs(node.val - target)
                closest = node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return closest
