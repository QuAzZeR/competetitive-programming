from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        answer = 0
        for i in range(k):
            v = happiness[i] - i
            if v > 0:
                answer += v
        return answer


print(Solution().maximumHappinessSum([1, 2, 3], 2))
print(Solution().maximumHappinessSum([1, 1, 1, 1], 2))
print(Solution().maximumHappinessSum([2, 3, 4, 5], 1))
