from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        count = 0
        if root is None:
            return 0
        q = deque()
        q.append(root)
        while q:
            count += 1
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return count


"""OPTIMIZED CODE
The timing complexity of this method is O(log(n)) for tree traversal, 
and worst case O(log(n)) for searching the last row. 
So the overall complexity is O((log(n)) ^ 2)."""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def lheight(node):
            if not node:
                return 0
            return 1 + lheight(node.left)

        def rheight(node):
            if not node:
                return 0
            return 1 + rheight(node.right)

        # BALANCED WHEN lheight = rheight

        l = lheight(root)
        r = rheight(root)

        if l > r:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        else:
            return (2 ** l) - 1

