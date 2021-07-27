from collections import deque


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        if not head:
            return

        q = deque()
        node = head
        while True:
            node = node.next
            if not node:
                break
            q.append(node)

        while q:
            if head:
                temp = q.pop()
                head.next = temp
                head = head.next

            if head and q:
                temp = q.popleft()
                head.next = temp
                head = head.next

        head.next = None