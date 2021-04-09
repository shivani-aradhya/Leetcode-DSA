# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        this_level = [root]
        next_level = []
        stack = []
        stack.append([root.val])
        
        while this_level:
            temp =[]    
            for n in this_level:
                if n.left is not None:
                    next_level.append(n.left)
                    temp.append(n.left.val)
                if n.right is not None:
                    next_level.append(n.right)
                    temp.append(n.right.val)
        
            if temp:
                stack.append(temp)
            
            this_level = next_level
            next_level = []

        stack.reverse()
        # stack[::-1]
        return stack