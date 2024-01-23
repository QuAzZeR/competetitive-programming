from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        if  n == 3:
            return sum(nums)
        m = float('inf')
        for i in range(1, n):
            for j in range(i+1, n):
                s = nums[0] + nums[i] + nums[j]
                if s < m:
                    m = s
        return int(m)

print(Solution().minimumCost([1,2,3,12]))
print(Solution().minimumCost([5,4,3]))
print(Solution().minimumCost([10,3,1,1]))
