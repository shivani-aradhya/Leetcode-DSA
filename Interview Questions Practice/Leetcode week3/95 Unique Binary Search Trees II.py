# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def helper(start, end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            res = []
            for i in range(start, end + 1):
                subtreeLeft = helper(start, i - 1)
                subtreeRight = helper(i + 1, end)

                for l in subtreeLeft:
                    for r in subtreeRight:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res

        return helper(1, n)

