from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        n = len(nums)
        for i in range(n):
            right -= nums[i]
            if i == 0:
                if left == right:
                    return i
                continue

            left += nums[i - 1]
            if left == right:
                return i
        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
print(Solution().pivotIndex([1, 2, 3]))
print(Solution().pivotIndex([2, 1, -1]))
print(Solution().pivotIndex([1, -1, 2]))
