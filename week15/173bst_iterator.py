# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.push(root)

    def push(self, node):                #Function created to push all left nodes
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        tmp = self.stack.pop()
        self.push(tmp.right)             #Call function in case of right node
        return tmp.val

    def hasNext(self) -> bool:
        return self.stack
