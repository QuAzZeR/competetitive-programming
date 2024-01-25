from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        answer = 0
        while sum(nums) != 0:
            nums = list(set([i for i in nums if i != 0]))
            m = min(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue
                nums[i] -= m
            answer += 1
        return answer

print(Solution().minimumOperations([1,5,0,3,5]))
print(Solution().minimumOperations([0]))
