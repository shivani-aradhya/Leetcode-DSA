class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        if head is None:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next