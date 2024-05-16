from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        l = []
        while head is not None:
            if head.val != val:
                l.append(head)
            head = head.next
        nxt = None
        while l:
            head = l.pop()
            head.next = nxt
            nxt = head
        return head
