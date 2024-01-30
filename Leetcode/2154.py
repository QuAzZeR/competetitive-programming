from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original *= 2
        return original


print(Solution().findFinalValue([5, 3, 6, 1, 12], 3))
print(Solution().findFinalValue([2, 7, 9], 4))
