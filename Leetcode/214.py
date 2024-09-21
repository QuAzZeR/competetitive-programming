from typing import List
import unittest


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        ss = s + '#' + s[::-1]
        n = len(ss)
        pi = [0] * n
        i = 1
        k = 0
        while i < n:
            if ss[i] == ss[k]:
                k += 1
                pi[i] =k
                i += 1
            else:
                if k > 0:
                    k = pi[k-1]
                else:
                    pi[i] = 0
                    i += 1
        return s[pi[-1]:][::-1] + s


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.shortestPalindrome("aaacecaaa"), "aaacecaaa")
        self.assertEqual(s.shortestPalindrome("abcd"), "dcbabcd")


if __name__ == "__main__":
    unittest.main()
