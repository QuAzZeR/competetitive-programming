from typing import List
import unittest


class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        answer = 0
        zero = 0
        for i in range(n):
            if s[i] == '0':
                answer += zero
            else:
                zero += 1
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minimumSteps("101"), 1)
        self.assertEqual(s.minimumSteps("100"), 2)
        self.assertEqual(s.minimumSteps("0111"), 0)


if __name__ == "__main__":
    unittest.main()
