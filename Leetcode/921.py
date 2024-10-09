from typing import List
import unittest


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ss = []
        for i in s:
            if i == '(':
                ss.append('(')
            else:
                if len(ss) > 0 and ss[-1] == '(':
                    ss.pop()
                else:
                    ss.append(')')
        return len(ss)


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == "__main__":
    unittest.main()
