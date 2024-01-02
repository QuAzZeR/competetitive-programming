from typing import List
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            answer.append(nums[i])
        return answer

print(Solution().buildArray([0,2,1,5,3,4]))
print(Solution().buildArray([5,0,1,2,3,4]))
