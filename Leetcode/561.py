from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        nums = sorted(nums)
        for i in range(0, len(nums), 2):
            answer += min(nums[i], nums[i+1])
        return answer

print(Solution().arrayPairSum([1,4,3,2]))
print(Solution().arrayPairSum([6,2,6,5,1,2]))
