from typing import List
from heapq import heappush, heappop
import unittest


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h = []
        k = len(nums)
        m = float('-inf')
        for i in range(k):
            heappush(h, (nums[i][0], i, 0))
            m = max(m, nums[i][0])
        r = [float('-inf'), float('inf')]
        while h:
            cm, idx, i = heappop(h)
            if (m -cm < r[1] - r[0]) or ((m - cm == r[1] - r[0]) and cm < r[0]):
                r = [cm, m]
            if i+1 < len(nums[idx]):
                heappush(h, (nums[idx][i+1], idx, i+1))
                m = max(m, nums[idx][i+1])
            else:
                break
        return r


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]), [20,24])
        self.assertEqual(s.smallestRange([[1,2,3],[1,2,3],[1,2,3]]), [1,1])


if __name__ == "__main__":
    unittest.main()
