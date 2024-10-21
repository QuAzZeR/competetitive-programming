from typing import List
import unittest


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, seen):
            if start == len(s):
                return 0
            m = 0
            for i in range(start +1 , len(s) + 1):
                ss = s[start:i]
                if ss not in seen:
                    seen.add(ss)
                    m = max(m, 1 + backtrack(i, seen))
                    seen.remove(ss)
            return m
        return backtrack(0, set())


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.maxUniqueSplit("ababccc"), 5)
        self.assertEqual(s.maxUniqueSplit('aba'), 2)
        self.assertEqual(s.maxUniqueSplit('aa'), 1)


if __name__ == "__main__":
    unittest.main()
