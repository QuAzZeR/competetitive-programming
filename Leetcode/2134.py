from typing import List
import unittest


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = sum(nums)
        if ones == 0 or ones == n:
            return 0
        current = sum(nums[:ones])
        m = current
        for i in range(n):
            current -= nums[i]
            current += nums[(i+ones) %n]
            m = max(m, current)
        return ones - m





class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minSwaps([0,1,0,1,1,0,0]), 1)
        self.assertEqual(s.minSwaps([0,1,1,1,0,0,1,1,0]), 2)
        self.assertEqual(s.minSwaps([1,1,0,0,1]), 0)


if __name__ == "__main__":
    unittest.main()
