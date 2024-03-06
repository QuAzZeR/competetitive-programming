from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        x = {}
        while head is not None:
            if head in x:
                return True
            x[head] = 1
            head = head.next
        return False
