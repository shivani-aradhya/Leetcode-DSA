# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node, parent_stolen):
            if not node:
                return 0

            if parent_stolen:
                # steal from parent

                return helper(node.left, False) + helper(node.right, False)

            else:

                # stealing at the current node
                steal = node.val + helper(node.left, True) + helper(node.right, True)

                # NOT stealing current node
                not_stealing = helper(node.left, False) + helper(node.right, False)

                return max(steal, not_stealing)

        return helper(root, False)