from typing import List
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        n  = sorted(nums, reverse=True)
        answer = (n[0] * n[1]) - (n[-1]*n[-2])
        return answer
print(Solution().maxProductDifference([5,6,2,7,4]))
print(Solution().maxProductDifference([4,2,5,9,7,4,8]))
