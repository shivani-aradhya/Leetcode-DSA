# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insertionSortList(self, head):
        dummyhead = ListNode()
        curr = head

        while curr:
            prev = dummyhead
            next = dummyhead.next

            while next:

                if curr.val < next.val:
                    break

                prev = prev.next
                next = next.next

            temp = curr.next

            curr.next = next
            prev.next = curr

            curr = temp

        return dummyhead.next