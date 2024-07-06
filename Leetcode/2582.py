import unittest
from typing import List


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        p = 1
        d = 1
        for _ in range(time):
            if p == n:
                d = -1
            if p == 1:
                d = 1
            p += d
        return p


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.passThePillow(4, 5), 2)
        self.assertEqual(s.passThePillow(3, 2), 3)


if __name__ == "__main__":
    unittest.main()
