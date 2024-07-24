from typing import List
import unittest


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.sortArray([5,2,3,1]), [1,2,3,5])

        self.assertEqual(s.sortArray([5,1,1,2,0,0]), [0,0,1,1,2,5])


if __name__ == "__main__":
    unittest.main()
