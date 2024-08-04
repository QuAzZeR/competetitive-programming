from typing import List
import unittest


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        answer = 0
        a = []
        for i in range(n):
            s = 0
            for j  in range(i, n):
                s += nums[j]
                a.append(s)
        a.sort()
        return sum(a[left - 1 : right]) %(10**9 +7)


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.rangeSum([1,2,3,4], 4,1,5), 13)
        self.assertEqual(s.rangeSum([1,2,3,4], 4, 3,4), 6)
        self.assertEqual(s.rangeSum([1,2,3,4], 4, 1,10), 50)


if __name__ == "__main__":
    unittest.main()
