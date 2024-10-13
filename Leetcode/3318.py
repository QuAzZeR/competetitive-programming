from typing import List
from collections import Counter
import unittest


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []
        n = len(nums)
        for i in range(n - k+1):
            d = Counter(nums[i:i+k])
            d = sorted([(j, d[j]) for j in d], key=lambda x: (-x[1],-x[0]))
            s = 0
            m = min(len(d), x)
            for j in range(m):
                s += d[j][0] * d[j][1]
            answer.append(s)
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.findXSum([1,1,2,2,3,4,2,3], 6, 2), [6,10,12])
        self.assertEqual(s.findXSum([3,8,7,8,7,5], 2,2), [11,15,15,15,12])
        self.assertEqual(s.findXSum([9,2,2], 3,3), [13])


if __name__ == "__main__":
    unittest.main()
