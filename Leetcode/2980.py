from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return sum(1 for i in nums if i % 2 == 0) >= 2


print(Solution().hasTrailingZeros([1, 2, 3, 4, 5]))
print(Solution().hasTrailingZeros([2, 4, 8, 16]))
print(Solution().hasTrailingZeros([1, 3, 5, 7, 9]))
