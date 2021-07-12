# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy

        while head:
            if head.next and head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                slow.next = head.next
            else:
                slow = slow.next

            head = head.next

        return dummy.next