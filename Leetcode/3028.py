from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        answer = 0
        position = 0
        for num in nums:
            position += num
            if position == 0:
                answer += 1
        return answer


print(Solution().returnToBoundaryCount([3, 2, -5]))
print(Solution().returnToBoundaryCount([3, 2, -3, -4]))
