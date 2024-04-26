from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[100 * n] * n for _ in range(n)]
        for j in range(n):
            dp[0][j] = grid[0][j]
        for i in range(1, n):
            for j in range(n):
                t = 100 * n
                for k in range(n):
                    if j != k:
                        t = min(t, grid[i][j] + dp[i - 1][k])
                dp[i][j] = t
        return min(dp[n - 1])


print(Solution().minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().minFallingPathSum([[7]]))
