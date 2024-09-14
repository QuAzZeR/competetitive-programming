from typing import List
import unittest


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        j = -1
        max_value = max(nums)
        answer = 0
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num != max_value:
                j = i
            answer = max(answer, i-j)
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.longestSubarray([1,2,3,3,2,2]), 2)
        self.assertEqual(s.longestSubarray([1,2,3,4]), 1)


if __name__ == "__main__":
    unittest.main()
