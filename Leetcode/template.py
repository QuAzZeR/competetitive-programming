from typing import List
import unittest


class Solution:
    def temp(self):
        pass


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.temp(), 3)
        self.assertEqual(s.temp(), 1)


if __name__ == "__main__":
    unittest.main()
