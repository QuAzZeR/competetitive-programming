from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        n = len(rewardValues)
        rewardValues.sort()
        dp = [[-1] * (4000) for _ in range(n + 1)]

        def binarySearch(i, x):
            if i >= n:
                return 0
            if dp[i][x] != -1:
                return dp[i][x]
            use = 0
            if x < rewardValues[i]:
                use = rewardValues[i] + binarySearch(i + 1, x + rewardValues[i])
            not_use = binarySearch(i + 1, x)
            dp[i][x] = max(use, not_use)
            return dp[i][x]

        return binarySearch(0, 0)


print(Solution().maxTotalReward([1, 1, 3, 3]))
print(Solution().maxTotalReward([1, 6, 4, 3, 2]))
print(Solution().maxTotalReward([4, 6]))
