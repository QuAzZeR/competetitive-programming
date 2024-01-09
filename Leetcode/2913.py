from typing import List
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        l = len(nums)
        sum = 0
        for i in range(1,l+1) :
            for j in range(0,l-i+1):
                current = nums[j:j+i]
                sum += len(set(current))**2
        return sum
print(Solution().sumCounts([1,2,1]))
print(Solution().sumCounts([1,2,1,3,4]))
print(Solution().sumCounts([1,1]))
