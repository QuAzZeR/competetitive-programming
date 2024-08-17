from typing import List
import unittest


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = points[0]
        for i in range(1,m):
            l_max = [0] * n
            r_max = [0] * n
            new_dp = [0] * n
            l_max[0] = dp[0]
            for j in range(1,n):
                l_max[j] = max(l_max[j-1], dp[j] + j)
            r_max[-1] = dp[-1] - (n-1)
            for j in range(n-2, -1, -1):
                r_max[j] = max(r_max[j+1], dp[j] - j)
            for j in range(n):
                new_dp[j] = max(l_max[j]-j, r_max[j] +j) + points[i][j]
            dp = new_dp
        return max(dp)


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.maxPoints([[1,2,3],[1,5,1],[3,1,1]]), 9)
        self.assertEqual(s.maxPoints([[1,5],[2,3],[4,2]]), 11)


if __name__ == "__main__":
    unittest.main()
