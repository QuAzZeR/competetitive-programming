from typing import List


class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        answer = []
        n = len(nums)
        k = 0
        seen = []
        for i in range(n):
            if nums[i] > 0:
                k = 0
                seen.append(nums[i])
            else:
                k += 1
                if k <= len(seen):
                    answer.append(seen[-k])
                else:
                    answer.append(-1)
        return answer


print(Solution().lastVisitedIntegers([1, 2, -1, -1, -1]))
print(Solution().lastVisitedIntegers([1, -1, 2, -1, -1]))
