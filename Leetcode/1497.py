from typing import List
import unittest


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        f = [0] * k

        for i in arr:
            r = i % k
            if r < 0:
                r += k
            f[r] += 1

        if f[0] %2 != 0:
            return False

        for i in range(1, (k //2) + 1):
            if f[i] != f[k-i]:
                return False

        return True


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.canArrange([1,2,3,4,5,10,6, 7,8,9], 5), True)
        self.assertEqual(s.canArrange([1,2,3,4,5,6], 7), True)
        self.assertEqual(s.canArrange([1,2,3,4,5,6], 10), False)


if __name__ == "__main__":
    unittest.main()
