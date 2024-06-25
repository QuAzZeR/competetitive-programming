from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        answer = float("inf")
        i = 0
        nums.sort()
        n = len(nums)
        for i in range(n // 2):
            answer = min(answer, (nums[i] + nums[n - i - 1]) / 2)
        return answer


print(Solution().minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]))
print(Solution().minimumAverage([1, 9, 8, 3, 10, 5]))
print(Solution().minimumAverage([1, 2, 3, 7, 8, 9]))
