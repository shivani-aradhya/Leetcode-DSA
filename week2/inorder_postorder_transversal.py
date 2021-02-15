class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(inorder):
            if inorder:
                middle = postorder.pop()
                index = inorder.index(middle)
                root = TreeNode(middle)
                root.right = build(inorder[index+1:])
                root.left = build(inorder[:index])
                return root
            else:
                return
        return build(inorder)