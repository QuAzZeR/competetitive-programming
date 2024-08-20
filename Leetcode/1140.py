from typing import List
import unittest


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        answer = 0
        n = len(piles)
        dp = [[0] * (n+1) for _ in range(n+1)]
        suffixSum = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suffixSum[i] = suffixSum[i+1] + piles[i]
        for i in range(n-1,-1,-1):
            for M in range(1, n+1):
                for X in range(1, min(2*M, n-i) + 1):
                    dp[i][M] = max(dp[i][M], suffixSum[i] - dp[i+X][max(M,X)])
        return dp[0][1]


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.stoneGameII([2,7,9,4,4]), 10)
        self.assertEqual(s.stoneGameII([1,2,3,4,5,100]), 104)


if __name__ == "__main__":
    unittest.main()
