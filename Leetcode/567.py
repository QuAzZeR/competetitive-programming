from typing import List
import unittest
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n2 < n1:
            return False
        f1 = Counter(s1)
        f2 = Counter(s2[0:n1])
        if f1 == f2:
            return True

        for i in range(n1, n2):
            f2[s2[i]] += 1
            f2[s2[i - n1]] -= 1
            if f2[s2[i - n1]] == 0:
                del f2[s2[i - n1]]
            if f1 == f2:
                return True

        return False


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.checkInclusion("ab", "eidbaooo"), True)
        self.assertEqual(s.checkInclusion("ab", "eidboaoo"), False)


if __name__ == "__main__":
    unittest.main()
