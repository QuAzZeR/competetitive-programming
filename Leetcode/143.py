from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        value = []
        current = head
        while current is not None:
            value.append(current.val)
            current = current.next
        current = head
        l = len(value) - 1
        i = 1
        c = 1
        while c < len(value):
            v = 0
            if c % 2 == 0:
                v = value[i]
                i += 1
            if c % 2 != 0:
                v = value[l]
                l -= 1
            current.next = ListNode(v)
            current = current.next
            c += 1
