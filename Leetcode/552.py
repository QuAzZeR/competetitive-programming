class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[1] * 3 for _ in range(2)]
        for i in range(1, n + 1):
            current_dp = [[0] * 3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    current_dp[a][l] += dp[a][2]
                    current_dp[a][l] %= MOD
                    if a > 0:
                        current_dp[a][l] += dp[a - 1][2]
                        current_dp[a][l] %= MOD
                    if l > 0:
                        current_dp[a][l] += dp[a][l - 1]
                        current_dp[a][l] %= MOD
            dp = current_dp
        return dp[1][2]


print(Solution().checkRecord(2))
print(Solution().checkRecord(1))
print(Solution().checkRecord(10101))
