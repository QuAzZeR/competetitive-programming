from typing import List
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            answer.append(len(set(nums[0:i+1]))- len(set(nums[i+1:])))
        return answer
print(Solution().distinctDifferenceArray([1,2,3,4,5]))
print(Solution().distinctDifferenceArray([3,2,3,4,2]))
