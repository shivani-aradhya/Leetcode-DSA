class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def treePathsSumUtil(root, val):

    if root is None:
        return 0

    val = (val * 10 + root.data)

    if root.left is None and root.right is None:
        return val

    return (treePathsSumUtil(root.left, val) +
            treePathsSumUtil(root.right, val))
def treePathsSum(root):
    return treePathsSumUtil(root, 0)

root = Node(6)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(4)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
print("Sum of all paths is", treePathsSum(root))
