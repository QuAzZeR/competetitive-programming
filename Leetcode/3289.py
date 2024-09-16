from typing import List
from collections import Counter
import unittest


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        c = Counter(nums)
        for i in c:
            if c[i] == 2:
                answer.append(i)
        return sorted(answer)


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.getSneakyNumbers([0,1,1,0]), [0,1])
        self.assertEqual(s.getSneakyNumbers([0,3,2,1,3,2]), [2,3])
        self.assertEqual(s.getSneakyNumbers( [7,1,5,4,3,4,6,0,9,5,8,2]), [4,5])


if __name__ == "__main__":
    unittest.main()
