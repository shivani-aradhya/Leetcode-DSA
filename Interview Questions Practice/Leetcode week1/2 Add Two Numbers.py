# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = dummy = ListNode(0)
        if not l1:
            return l2
        if not l2:
            return l1

        carry = 0
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            sum = carry % 10
            carry = carry // 10
            node = ListNode(sum)
            curr.next = node
            curr = curr.next
            
        #EDGE CASE WHEN CARRY =1
        if carry > 0:
            curr.next = ListNode(carry)

        return dummy.next