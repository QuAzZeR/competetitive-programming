from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head is not None:
            while l and l[-1].val < head.val:
                l.pop()
            l.append(head)
            head = head.next
        nxt = None
        while l:
            head = l.pop()
            head.next = nxt
            nxt = head
        return head
