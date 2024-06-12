from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()


print(Solution().sortColors([2, 0, 2, 1, 1, 0]))
print(Solution().sortColors([2, 0, 1]))
