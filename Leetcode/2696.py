from typing import List
import unittest


class Solution:
    def minLength(self, s: str) -> int:
        pre_len = 0
        cur_len = len(s)
        while pre_len != cur_len:
            pre_len = cur_len
            for i in range(cur_len-1):
                if s[i:i+2] in  ['AB', 'CD']:
                    s = s[0:i] +s[i+2:]
                    break

            cur_len =  len(s)
        return cur_len


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minLength("ABFCACDB"), 2)
        self.assertEqual(s.minLength("ACBBD"), 5)


if __name__ == "__main__":
    unittest.main()
