from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                l = nums[:i] + nums[j:]
                if l == sorted(l) and len(l) == len(set(l)):
                    answer += 1

        return answer


print(Solution().incremovableSubarrayCount([1, 2, 3, 4]))
print(Solution().incremovableSubarrayCount([5, 3, 4, 6, 7]))
print(Solution().incremovableSubarrayCount([6, 5, 7, 8]))
print(Solution().incremovableSubarrayCount([8, 7, 6, 6]))
