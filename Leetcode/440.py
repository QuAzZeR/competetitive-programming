from typing import List
import unittest


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def get_num(a, b, nn):
            gap = 0
            while a <= nn:
                gap += min(nn+1, b) - a
                a *= 10
                b *= 10
            return gap
        answer = 1
        i = 1
        while i < k:
            r = get_num(answer, answer+1, n)
            if i + r <= k:
                i += r
                answer += 1
            else:
                i += 1
                answer *= 10
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.findKthNumber(13, 2), 10)
        self.assertEqual(s.findKthNumber(1, 1), 1)
        self.assertEqual(s.findKthNumber(2, 2), 2)


if __name__ == "__main__":
    unittest.main()
