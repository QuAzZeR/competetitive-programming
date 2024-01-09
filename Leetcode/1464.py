from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = 0
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                m = max(m, (nums[i]-1)*(nums[j]-1))
        return m
print(Solution().maxProduct([3,4,5,2]))
print(Solution().maxProduct([1,5,4,5]))
print(Solution().maxProduct([3,7]))
