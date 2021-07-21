# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder)==0:
            return
        if len(preorder)==1:
            return TreeNode(preorder[0])

        root_val= preorder.pop(0)
        root= TreeNode(root_val)
        index_root= inorder.index(root_val)

        root.left = self.buildTree(preorder, inorder[:index_root])  # 4
        root.right = self.buildTree(preorder, inorder[index_root + 1:])
        return root
