from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = 0
        c = 0
        if nums[0] == 1:
            c += 1
        for i in range(1, len(nums)):
            if nums[i] == 1:
                c += 1
            else:
                answer = max(c, answer)
                c = 0
        answer = max(c, answer)
        return answer


print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
