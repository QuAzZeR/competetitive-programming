from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        l = len(nums)
        dp = [1] * l
        ms, mi = 1, 0
        for i in range(l):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > ms:
                        ms = dp[i]
                        mi = i
        answer = []
        num = nums[mi]
        for i in range(mi, -1, -1):
            if dp[i] == ms and num % nums[i] == 0:
                answer.append(nums[i])
                num = nums[i]
                ms -= 1
        return answer


print(Solution().largestDivisibleSubset([1, 2, 3]))
print(Solution().largestDivisibleSubset([1, 2, 4, 8]))
