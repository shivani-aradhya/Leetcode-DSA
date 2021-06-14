# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return

        while root:

            parent = root.val
            if p.val > parent and q.val > parent:
                root = root.right
            elif p.val < parent and q.val < parent:
                root = root.left
            else:
                return root