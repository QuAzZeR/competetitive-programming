from typing import List
import unittest


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        answer = 0
        s_time = sorted(i[0] for i in intervals)
        e_time = sorted(i[1] for i in intervals)
        e_idx = 0
        for s in s_time:
            if s > e_time[e_idx]:
                e_idx += 1
            else:
                answer += 1
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]), 3)
        self.assertEqual(s.minGroups([[1,3],[5,6],[8,10],[11,13]]), 1)


if __name__ == "__main__":
    unittest.main()
