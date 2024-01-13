from typing import List
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 2:
            return -1

        nums = sorted(nums)
        return nums[1]
print(Solution().findNonMinOrMax([3,2,1,4]))
print(Solution().findNonMinOrMax([1,2]))
print(Solution().findNonMinOrMax([2,1,3]))
