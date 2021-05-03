# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):

        '''left---right---root'''

        stack =[root]
        result=[]
        while stack:
            root = stack.pop()
            if root:
                result.insert(0, root.val)
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)

        return result