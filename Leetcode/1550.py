from typing import List
import unittest


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c = 0
        for a in arr:
            if a % 2 != 0:
                c += 1
            else:
                c = 0
            if c == 3:
                return True
        return False


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.threeConsecutiveOdds([2, 6, 4, 1]), False)
        self.assertEqual(s.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]), True)


if __name__ == "__main__":
    unittest.main()
