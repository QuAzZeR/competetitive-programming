# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = 0
        factor = 1
        temp = ''
        while head:
            temp += str(head.val)
            head = head.next
        for i in temp[::-1]:
            answer += int(i)*factor
            factor *=2
        return answer
