from typing import List, Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        while head and head.val in s:
            head = head.next
        p = head
        c = head.next
        while c :
            if c.val not in s:
                p.next = c
                p = c
            c = c.next
        p.next = None
        return head



if __name__ == "__main__":
    unittest.main()
