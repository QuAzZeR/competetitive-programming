from typing import List
import unittest


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def count(d):
            c = 0
            j = 0
            for i in range(1, len(nums)):
                while nums[i] - nums[j] > d:
                    j += 1
                c += i - j
            return c
        min_d = 0
        max_d = nums[-1] - nums[0]
        while min_d < max_d:
            mid_d = (min_d + max_d) // 2
            if count(mid_d) < k:
                min_d = mid_d + 1
            else:
                max_d = mid_d
        return min_d


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.smallestDistancePair([1,3,1], 1), 0)
        self.assertEqual(s.smallestDistancePair([1,1,1], 2), 0)
        self.assertEqual(s.smallestDistancePair([1,6,1], 3), 5)


if __name__ == "__main__":
    unittest.main()
