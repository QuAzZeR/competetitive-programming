from typing import List
import unittest


class Solution:
    def minimumDeletions(self, s: str) -> int:
        answer = 0
        c = 0
        for i in s:
            if i == 'b':
                c += 1
            elif c:
                answer += 1
                c -= 1
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minimumDeletions("aababbab"), 2)
        self.assertEqual(s.minimumDeletions("bbaaaaabb"), 2)


if __name__ == "__main__":
    unittest.main()
