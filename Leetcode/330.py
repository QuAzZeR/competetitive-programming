from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missing = 1
        answer = 0
        i = 0
        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                missing += missing
                answer += 1
        return answer


print(Solution().minPatches([1, 3], 6))
print(Solution().minPatches([1, 5, 10], 20))
print(Solution().minPatches([1, 2, 2], 5))
