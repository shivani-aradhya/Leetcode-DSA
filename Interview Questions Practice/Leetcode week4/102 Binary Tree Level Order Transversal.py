from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root: return [] #base case
        res = []

        queue = deque([root])

        while queue:
            level_vals = [] #hold the values at the current level.
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_vals.append(node.val)
            res.append(level_vals)
        return res