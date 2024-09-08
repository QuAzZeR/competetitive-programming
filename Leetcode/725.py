from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        answer = [None] * k
        c = head
        n = 0
        while c:
            n += 1
            c = c.next
        s = n // k
        r = n % k
        c = head
        for i in range(k):
            answer[i] = c
            cs = s + (1 if r > 0 else 0)
            r -= 1
            for _ in range(cs -1):
                if c:
                    c = c.next
            if c:
                temp = c.next
                c.next = None
                c = temp
        return answer
