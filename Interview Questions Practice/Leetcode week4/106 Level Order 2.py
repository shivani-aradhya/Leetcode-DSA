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

        queue = [root]
        result = []

        while (len(queue) != 0):
            l = []
            for i in range(len(queue)):
                temp = queue.pop(0)
                l.append(temp.data)
                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)

                result.insert(0, l)
        return result

    