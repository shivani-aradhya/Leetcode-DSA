class Node:
    def __init__(self,data):
        self.data= data
        self.left= None
        self.right=None

def zigzag(root):
    if root is None:
        return []

    s1= [root]
    s2= []
    level=[]
    result =[]

    while s1 or s2:
        while s1:
            node = s1.pop()
            level.append(node.data)
            if node.left:
                s2.append(node.left)
            if node.right:
                s2.append(node.right)
        result.append(level)
        level= []

        while s2:
            node = s2.pop()
            level.append((node.data))
            if node.right:
                s1.append(node.right)
            if node.left:
                s1.append((node.left))

        if level != []:
            result.append(level)
            level = []
    return result