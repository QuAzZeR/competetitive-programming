from typing import List
import unittest
from heapq import heapify, heappop, heappush


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        answer = 0
        heapify(pq:=[-x for x in nums])
        for i in range(k):
            x =-heappop(pq)
            answer += x
            if x == 1:
                answer += k - 1 - i
                break
            heappush(pq, -((x+2)//3))

        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.maxKelements([10,10,10,10,10], 5), 50)
        self.assertEqual(s.maxKelements([1,10,3,3,3],3), 17)


if __name__ == "__main__":
    unittest.main()
