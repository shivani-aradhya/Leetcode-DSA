# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result =[]
        queue =[root]
        level =[]         #to store child nodes
        while queue:
            for root in queue:
                if root.left:
                    level.append(root.left)

                if root.right:
                    level.append(root.right)

            result.append(root.val)
            queue = level
            level =[]
        return result