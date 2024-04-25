class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 129
        for i in s:
            j = ord(i)
            dp[j] = max(dp[j - k : j + k + 1]) + 1
        return max(dp)


print(Solution().longestIdealString("acfgbd", 2))
print(Solution().longestIdealString("abcd", 3))
