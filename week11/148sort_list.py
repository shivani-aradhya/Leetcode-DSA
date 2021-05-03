# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):

        if not head or not head.next:
            return head

        p, slow, fast = None, head, head

        while fast and fast.next:
            p = slow
            slow = slow.next
            fast = fast.next.next

        p.next = None
        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right)

    def merge(self, left, right):

        dummy = ListNode()
        curr = dummy

        while left and right:
            if left.val > right.val:
                curr.next = right
                right = right.next

            else:
                curr.next = left
                left = left.next
            curr = curr.next

        if left:
            curr.next = left
        if right:
            curr.next = right

        return dummy.next

