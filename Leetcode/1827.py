from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        answer = 0
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                continue
            df = abs(nums[i] - nums[i-1])
            nums[i] += df +1
            answer += df+1
        return answer
print(Solution().minOperations([1,1,1]))
print(Solution().minOperations([1,5,2,4,1]))
print(Solution().minOperations([8]))
