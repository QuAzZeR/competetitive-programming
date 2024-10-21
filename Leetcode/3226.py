from typing import List
import unittest


class Solution:
    def minChanges(self, n: int, k: int) -> int:

        bn = bin(n).split('b')[-1]
        bk = bin(k).split('b')[-1]
        answer = 0
        m = max(len(bn), len(bk))
        bn = '0'*(m - len(bn)) + bn
        bk = '0'*(m - len(bk)) + bk
        for i in range(m):
            if bn[i] == '1' and bk[i] == '0':
                answer += 1
            if bn[i] == '0' and bk[i] == '1':
                return -1
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minChanges(13, 4), 2)
        self.assertEqual(s.minChanges(21, 21), 0)
        self.assertEqual(s.minChanges(14, 13), -1)


if __name__ == "__main__":
    unittest.main()
