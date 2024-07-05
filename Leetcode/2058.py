from typing import List, Optional
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        index = []
        c = 1
        previous = 0
        while head is not None:
            if c == 1:
                previous = head.val
                head = head.next
                c += 1
                continue
            if head.next is None:
                head = head.next
                continue
            next = head.next.val
            current = head.val
            if current < next and current < previous:
                index.append(c)
            if current > next and current > previous:
                index.append(c)
            previous = current
            head = head.next
            c += 1
        if len(index) <= 1:
            return [-1, -1]
        index.sort()
        m = index[-1] - index[-2]
        for i in range(1, len(index)):
            m = min(index[i] - index[i - 1], m)
        return [m, index[-1] - index[0]]


def build_graph(l: List):
    if len(l) == 0:
        return None
    h = ListNode(l[0], None)
    current = h
    for i in range(1, len(l)):
        new = ListNode(l[i], None)
        current.next = new
        current = new
    return h


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.nodesBetweenCriticalPoints(build_graph([3, 1])), [-1, -1])
        self.assertEqual(
            s.nodesBetweenCriticalPoints(build_graph([5, 3, 1, 2, 5, 1, 2])), [1, 3]
        )
        self.assertEqual(
            s.nodesBetweenCriticalPoints(build_graph([1, 3, 2, 2, 3, 2, 2, 2, 7])),
            [3, 3],
        )

        self.assertEqual(
            s.nodesBetweenCriticalPoints(build_graph([2, 2, 1, 3])),
            [-1, -1],
        )

        self.assertEqual(
            s.nodesBetweenCriticalPoints(build_graph([6, 8, 4, 1, 9, 6, 6, 10, 6])),
            [1, 6],
        )


if __name__ == "__main__":
    unittest.main()
