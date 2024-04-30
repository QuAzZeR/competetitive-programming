from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        answer = 300
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        answer = min(answer, nums[i] + nums[j] + nums[k])

        if answer == 300:
            return -1
        return answer


print(Solution().minimumSum([8, 6, 1, 5, 3]))
print(Solution().minimumSum([5, 4, 8, 7, 10, 2]))
print(Solution().minimumSum([6, 5, 4, 3, 4, 5]))
