from typing import List
import unittest


class Solution:
    def strangePrinter(self, s: str) -> int:
        self.mem = {}
        def dp(i,j):
            if i  > j:
                return 0
            if (i,j) in self.mem:
                return self.mem[(i,j)]
            r = dp(i+1,j) + 1
            for k in range(i+1, j+1):
                if s[k] == s[i]:
                    r = min(r, dp(i,k-1) + dp(k+1, j))
            self.mem[(i,j)] = r
            return r
        return dp(0, len(s) - 1)


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.strangePrinter("aaabbb"), 2)
        self.assertEqual(s.strangePrinter("aba"), 2)


if __name__ == "__main__":
    unittest.main()
