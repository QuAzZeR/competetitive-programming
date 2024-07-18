from typing import List
import unittest


class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k %= n
        return s[k:] + s[:k]


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.getEncryptedString("dart", 3), "tdar")
        self.assertEqual(s.getEncryptedString("aaa", 1), "aaa")
        self.assertEqual(s.getEncryptedString("byd", 4), "ydb")


if __name__ == "__main__":
    unittest.main()
