from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        answer = [[-1] * n for _ in range(m)]
        top = 0
        bottom = m-1
        left = 0
        right = n-1
        while head:
            for c in range(left, right +1):
                if not head:
                    break
                answer [top][c] = head.val
                head = head.next
            top += 1
            for r in range(top, bottom+1):
                if not head:
                    break
                answer [r][right] = head.val
                head = head.next
            right -= 1

            for c in range(right, left - 1, -1):
                if not head:
                    break
                answer [bottom][c] = head.val
                head = head.next
            bottom -= 1

            for r in range(bottom, top-1 ,-1):
                if not head:
                    break
                answer [r][left] = head.val
                head = head.next
            left += 1

        return answer


