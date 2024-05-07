from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        v = 0
        while head:
            v = v * 10 + head.val
            head = head.next
        answer = None
        cur = answer
        v *= 2
        if v == 0:
            return ListNode(0, None)
        while v:
            x = v % 10
            v //= 10
            cur = answer
            answer = ListNode(x, cur)

        return answer
