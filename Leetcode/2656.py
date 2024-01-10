from typing import List
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        print(m)
        return k*(m) + (k-1)*(k)//2

print(Solution().maximizeSum([1,2,3,4,5],3))
print(Solution().maximizeSum([5,5],2))
