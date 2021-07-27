class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def clonegraph(node):
        if not node:
            return

        q = []
        q.append(node)
        d = {}

        while q:
            curr = q.pop(0)
            if curr not in d:
                d[curr] = Node(curr.val)

                for new in curr.neighbours:
                    if new not in d:
                        d[new] = Node(new.val)
                        q.append(new)
                    d[curr].neighbors.append(d[new])
        return d[node]