from typing import List
import unittest


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] == 1 and nums[n - 1] == n:
            return 0
        min_i = nums.index(1)
        max_i = nums.index(n)
        if min_i < max_i:
            return min_i + (n - 1 - max_i)
        elif min_i > max_i:
            return min_i + (n - 1 - max_i) - 1
        return 0


class Testcase(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.semiOrderedPermutation([2, 1, 4, 3]), 2)
        self.assertEqual(s.semiOrderedPermutation([2, 4, 1, 3]), 3)
        self.assertEqual(s.semiOrderedPermutation([1, 3, 4, 2, 5]), 0)


if __name__ == "__main__":
    unittest.main()
