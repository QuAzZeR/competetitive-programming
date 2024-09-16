from typing import List
import unittest


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        answer = 0
        n = len(s)
        ma = {
            'a': 1,
            'e': 2,
            'i': 4,
            'o': 8,
            'u': 16,
        }
        mask = 0
        m = [-2] * 32
        m[0] = -1
        for i in range(n):
            c = s[i]
            if c in ma:
                mask ^= ma[c]
            p = m[mask]
            if p == -2:
                m[mask] = i
            else:
                answer = max(answer, i - p)
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.findTheLongestSubstring("eleetminicoworoep"), 13)
        self.assertEqual(s.findTheLongestSubstring('leetcodeisgreat'), 5)
        self.assertEqual(s.findTheLongestSubstring('bcbcbc'), 6)


if __name__ == "__main__":
    unittest.main()
