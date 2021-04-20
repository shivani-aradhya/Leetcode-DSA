class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return []

        node = head
        while node:
            next = node.next
            copy = Node(node.val, node.next, node.random)
            node.next = copy
            copy.next = next
            node = next

        node = head

        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        dummy = Node(0)
        prev = dummy
        node = head

        while node:
            prev.next = node.next
            node.next = node.next.next
            node = node.next
            prev = prev.next

        return dummy.next
