from typing import List
import unittest


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        for i in range(k):
            m = min([[i, nums[i]] for i in range(n)], key=lambda x: (x[1],x[0]))
            nums[m[0]] = m[1] * multiplier
        return nums


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.getFinalState([2,1,3,5,6], 5, 2), [8,4,6,5,6])
        self.assertEqual(s.getFinalState([1,2], 3, 4), [16,8])


if __name__ == "__main__":
    unittest.main()
