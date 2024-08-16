from typing import List
import unittest


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        m = arrays[0][0]
        mx = arrays[0][-1]
        answer = 0
        for i in range(1,n):
            l,b = arrays[i][0], arrays[i][-1]
            answer = max(answer, abs(b - m), abs(mx - l))
            mx = max(mx,b)
            m = min(m,l)
        return answer



class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.maxDistance([[1,2,3],[4,5],[1,2,3]]), 4)
        self.assertEqual(s.maxDistance([[1], [1]]), 0)


if __name__ == "__main__":
    unittest.main()
