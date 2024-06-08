from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[1] * (k + 1) for _ in range(n)]
        answer = 1
        for i in range(1, n):
            for j in range(k + 1):
                for l in range(i):
                    if nums[l] == nums[i]:
                        dp[i][j] = max(dp[i][j], dp[l][j] + 1)
                    elif j > 0:
                        dp[i][j] = max(dp[i][j], dp[l][j - 1] + 1)
                answer = max(answer, dp[i][j])
        return answer


print(Solution().maximumLength([1, 2, 1, 1, 3], 2))
print(Solution().maximumLength([1, 2, 3, 4, 5, 1], 0))
