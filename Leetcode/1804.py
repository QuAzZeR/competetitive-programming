from typing import List
import unittest


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        remaining = k%total
        n = len(chalk)
        for i in range(n):
            if remaining < chalk[i]:
                return i
            remaining -= chalk[i]
        return 0


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.chalkReplacer([5,1,5], 22), 0)
        self.assertEqual(s.chalkReplacer([3,4,1,2], 25), 1)


if __name__ == "__main__":
    unittest.main()
