from typing import List
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(0, len(nums)):
            left_sum = sum(nums[0:i])
            right_sum = sum(nums[i+1:])
            answer.append(abs(left_sum - right_sum))
        return answer
print(Solution().leftRightDifference([10,4,8,3]))
print(Solution().leftRightDifference([1]))
