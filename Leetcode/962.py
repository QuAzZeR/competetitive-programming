from typing import List
import unittest


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        s = []
        for i in range(n):
            if not s or nums[s[-1]] > nums[i]:
                s.append(i)
        for i in range(n-1, -1 ,-1):
            while s and nums[s[-1]] <= nums[i]:
                answer =  max(answer, i - s.pop())
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.maxWidthRamp([6,0,8,2,1,5]), 4)
        self.assertEqual(s.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]), 7)


if __name__ == "__main__":
    unittest.main()
