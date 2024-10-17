from typing import List
import unittest


class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        d = {int(s[i]): i for i in range(n)}
        for i in range(n):
            for j in range(9, int(s[i]), -1):
                if d.get(j, -1) > i:
                    t = s[d[j]]
                    s[d[j]] = s[i]
                    s[i] = t
                    return int(''.join(s))
        return int(''.join(s))


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.maximumSwap(2736), 7236)
        self.assertEqual(s.maximumSwap(9973), 9973)
        self.assertEqual(s.maximumSwap(9937), 9973)
        self.assertEqual(s.maximumSwap(9139), 9931)
        self.assertEqual(s.maximumSwap(98368), 98863)


if __name__ == "__main__":
    unittest.main()
