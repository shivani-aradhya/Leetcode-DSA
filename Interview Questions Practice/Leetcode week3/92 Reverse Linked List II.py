# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return head
        if left == right:
            return head
        dummy = prev = ListNode(0, next=head)
        for i in range(left - 1):
            prev = prev.next

        curr = prev.next
        rev = None

        for i in range(right - left + 1):
            temp = curr.next
            curr.next = rev
            rev = curr
            curr = temp

        prev.next.next = curr
        prev.next = rev

        return dummy.next