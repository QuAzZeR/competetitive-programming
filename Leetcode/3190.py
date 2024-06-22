from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        answer = 0
        for i in nums:
            answer += min(i % 3, 3 - (i % 3))
        return answer


print(Solution().minimumOperations([1, 2, 3, 4]))
print(Solution().minimumOperations([3, 6, 9]))
