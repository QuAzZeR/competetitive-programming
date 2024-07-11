from typing import List
import unittest


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = []
        for i in logs:
            if i == "./":
                s = s
            elif i == "../":
                if len(s) != 0:
                    s.pop()
            else:
                s.append(i)
        return len(s)


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minOperations(["d1/", "d2/", "../", "d21/", "./"]), 2)
        self.assertEqual(s.minOperations(["d1/", "d2/", "./", "d3/", "../", "d31/"]), 3)
        self.assertEqual(s.minOperations(["d1/", "../", "../", "../"]), 0)


if __name__ == "__main__":
    unittest.main()
