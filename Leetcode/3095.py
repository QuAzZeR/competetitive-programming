from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # nums = sorted(nums, reverse=True)
        n = len(nums)
        x = nums[0]
        m = 5000
        for i in range(n):
            x = nums[i]
            if x >= k:
                return 1
            for j in range(i + 1, len(nums)):
                x |= nums[j]
                if x >= k:
                    m = min(m, j - i + 1)
        if m == 5000:
            return -1
        return m


print(Solution().minimumSubarrayLength([1, 2, 3], 2))
print(Solution().minimumSubarrayLength([2, 1, 8], 10))
print(Solution().minimumSubarrayLength([1, 2], 0))
print(Solution().minimumSubarrayLength([32, 2, 24, 1], 35))
print(Solution().minimumSubarrayLength([16, 1, 2, 20, 32], 45))
print(Solution().minimumSubarrayLength([32, 1, 25, 11, 2], 59))
