# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        curr = dummy
        for i in range(count - k):
            curr = curr.next

        prev = curr.next
        curr.next = None

        dummy.next = prev
        curr = dummy.next
        while curr.next:
            curr = curr.next
        curr.next = head

        return dummy.next
