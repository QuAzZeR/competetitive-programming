from typing import List
import unittest


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        answer = []
        n = len(nums)
        for i in nums:
            if i %2 == 0:
                answer.append(-1)
            else:
                answer.append(i -((i+1) & (-i -1))//2)
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minBitwiseArray([2,3,5,7]), [-1,1,4,3])
        self.assertEqual(s.minBitwiseArray([11,13,31]), [9,12,15])

if __name__ == "__main__":
    unittest.main()
