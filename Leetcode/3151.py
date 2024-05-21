from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        for i in range(1, n):
            if nums[i] % 2 == nums[i - 1] % 2:
                return False
        return True


print(Solution().isArraySpecial([1]))
print(Solution().isArraySpecial([2, 1, 4]))
print(Solution().isArraySpecial([4, 3, 1, 6]))
