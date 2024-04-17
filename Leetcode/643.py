from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums) / k
        s = sum(nums[:k])
        m = s / k
        n = len(nums)
        for i in range(k, n):
            s -= nums[i - k]
            s += nums[i]
            m = max(m, s / k)
        return m


print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(Solution().findMaxAverage([5], 1))
print(Solution().findMaxAverage([0, 1, 1, 3, 3], 4))
