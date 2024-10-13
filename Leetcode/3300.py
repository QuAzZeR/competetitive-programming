from typing import List
import unittest


class Solution:
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = sum([int(d) for d in str(nums[i])])
        return min(nums)


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minElement([10,12,13,14]), 1)
        self.assertEqual(s.minElement([1,2,3,4]), 1)
        self.assertEqual(s.minElement([999,19,199]), 10)


if __name__ == "__main__":
    unittest.main()
