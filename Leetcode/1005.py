from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        i = 0
        while k > 0 and i < n:
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
            i += 1
        nums = sorted(nums)
        if k > 0 and k % 2 != 0:
            nums[0] = -nums[0]
        return sum(nums)


print(Solution().largestSumAfterKNegations([4, 2, 3], 1))
print(Solution().largestSumAfterKNegations([3, -1, 0, 2], 3))
print(Solution().largestSumAfterKNegations([2, -3, -1, 5, -4], 2))
print(Solution().largestSumAfterKNegations([3, -1, 0, 2], 3))
print(Solution().largestSumAfterKNegations([-2, 9, 9, 8, 4], 5))
