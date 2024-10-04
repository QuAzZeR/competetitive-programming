from typing import List
import unittest


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(list(set(arr)))
        n = len(a)
        rank = {a[i]: i+1 for i in range(n)}
        return [rank[i] for i in arr]


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.arrayRankTransform([40,10,20,30]), [4,1,2,3])
        self.assertEqual(s.arrayRankTransform([100,100,100]), [1,1,1])
        self.assertEqual(s.arrayRankTransform([37,12,28,9,100,56,80,5,12]), [5,3,4,2,8,6,7,1,3])


if __name__ == "__main__":
    unittest.main()
