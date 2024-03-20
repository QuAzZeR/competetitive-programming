# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        head = list1
        point1 = None
        point2 = None
        c = 0
        while list1 is not None:
            if c == a - 1:
                point1 = list1
            if c == b + 1:
                point2 = list1
            c += 1
            list1 = list1.next

        point1.next = list2
        while list2.next is not None:
            list2 = list2.next
        list2.next = point2
        return head
