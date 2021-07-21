"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = [root]

        while q:
            curr = None
            nxt = None
            for i in range(len(q)):
                if curr is None:
                    curr = q.pop(0)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)

                elif nxt is None:
                    nxt = q.pop(0)
                    curr.next = nxt
                    if nxt.left:
                        q.append(nxt.left)
                    if nxt.right:
                        q.append(nxt.right)

                else:
                    curr = q.pop(0)
                    nxt.next = curr
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                    nxt = curr

        return root
