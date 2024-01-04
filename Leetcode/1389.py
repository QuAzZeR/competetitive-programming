from typing import List
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        answer = [nums[0]]
        for i in range(1, len(nums)):
            pre = []
            post = []
            current = [nums[i]]
            if index[i] > 0:
                pre = answer[0:index[i]]
            if index[i] < len(nums):
                post = answer[index[i]:]
            answer = pre + current +post
        return answer


print(Solution().createTargetArray([0,1,2,3,4], [0,1,2,2,1]))
print(Solution().createTargetArray([1,2,3,4,0],[0,1,2,3,0]))
print(Solution().createTargetArray([1],[0]))

