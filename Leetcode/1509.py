from typing import List
import unittest


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        k = len(nums) - 3
        answer = nums[-1] - nums[0]
        for i in range(k - 1, n):
            answer = min(answer, nums[i] - nums[i - k + 1])
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minDifference([5, 3, 2, 4]), 0)
        self.assertEqual(s.minDifference([1, 5, 0, 10, 14]), 1)
        self.assertEqual(s.minDifference([3, 100, 20]), 0)
        self.assertEqual(s.minDifference([6, 6, 0, 1, 1, 4, 6]), 2)


if __name__ == "__main__":
    unittest.main()
