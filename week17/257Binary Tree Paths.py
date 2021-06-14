# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        res = []
        stack = [(root, "")]

        while stack:
            node, s = stack.pop()

            if not node.left and not node.right:
                res.append(s + str(node.val))

            if node.right:
                stack.append((node.right, s + str(node.val) + '->'))

            if node.left:
                stack.append((node.left, s + str(node.val) + '->'))

        return res

"""String contains all left values to be added"""