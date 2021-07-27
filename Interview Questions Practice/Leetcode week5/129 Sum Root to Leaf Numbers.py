class Node:
    def __init__(self,data):
        self.data= data
        self.left= None
        self.right = None

def sumroot(root):
     return treepathsum(root,0)

def treepathsum(root, value):

    if root is None:
        return 0

    if root.left is None and root.right is None:
        return value

    return treepathsum(root.left, value)+ treepathsum(root.right, value)