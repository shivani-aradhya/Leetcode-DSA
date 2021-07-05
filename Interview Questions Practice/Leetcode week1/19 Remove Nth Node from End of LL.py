# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""OPTIMIZED"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        slow = fast = dummy
        #kEEPING SLOW AND FAST NODES N NODES APART
        for i in range(n + 1):
            fast = fast.next
       
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next

        l -= n
        curr = dummy
        for i in range(l):
            curr = curr.next
        curr.next = curr.next.next

        return dummy.next
