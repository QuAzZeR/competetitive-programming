from typing import List
import unittest


class Solution:
    def minSwaps(self, s: str) -> int:
        answer = 0
        for i in s:
            if i == '[':
                answer += 1
            elif answer > 0:
                answer -= 1

        return (answer + 1) // 2


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minSwaps('][]['), 1)
        self.assertEqual(s.minSwaps(']]][[['), 2)
        self.assertEqual(s.minSwaps('[]'), 0)


if __name__ == "__main__":
    unittest.main()
