from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        nums = sorted(nums)
        answer = nums[k - 1] - nums[0]
        for i in range(k, len(nums)):
            answer = min(answer, nums[i] - nums[i - k + 1])
        return answer


print(Solution().minimumDifference([90], 1))
print(Solution().minimumDifference([9, 4, 1, 7], 2))
print(Solution().minimumDifference([87063, 61094, 44530, 21297, 95857, 93551, 9918], 6))
