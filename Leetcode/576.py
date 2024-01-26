class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp =[[0]*n for _ in range(m)]
        dp[startRow][startColumn] = 1
        count = 0
        mod = 10**9 +7
        for move in range(1,maxMove+1):
            t =[[0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m-1:
                        count = (count + dp[i][j]) % mod
                    if i == 0:
                        count = (count + dp[i][j]) % mod
                    if j == n-1:
                        count = (count + dp[i][j]) % mod
                    if j == 0:
                        count = (count + dp[i][j]) % mod
                    t[i][j] = (((dp[i][j-1] if j > 0 else 0) + (dp[i][j+1] if j < n - 1 else 0)) % mod + ((dp[i-1][j] if i > 0 else 0) + (dp[i+1][j] if i < m - 1 else 0)) % mod) % mod
            dp = t
        return count

print(Solution().findPaths(2,2,2,0,0))
print(Solution().findPaths(1,3,3,0,1))
