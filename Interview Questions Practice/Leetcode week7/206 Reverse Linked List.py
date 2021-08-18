# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next  # Storing next node
            curr.next = prev  # Reversing link
            prev = curr  # Storing previous element
            curr = nxt  # Moving loop ahead

        return prev