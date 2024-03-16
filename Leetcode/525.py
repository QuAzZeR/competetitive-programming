from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = {}
        answer = 0
        current_sum = 0
        for i, num in enumerate(nums):
            current_sum += 1 if num == 1 else -1
            if current_sum == 0:
                answer = i + 1
            elif current_sum in count:
                answer = max(answer, i - count[current_sum])
            else:
                count[current_sum] = i
        return answer


print(Solution().findMaxLength([0, 1]))
print(Solution().findMaxLength([0, 1, 0]))
