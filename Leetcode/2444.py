from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_index = -1
        max_index = -1
        index = -1
        answer = 0
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if minK > num or num > maxK:
                index = i
            if minK == num:
                min_index = i
            if maxK == num:
                max_index = i
            answer += max(0, min(max_index, min_index) - index)
        return answer


print(Solution().countSubarrays([1, 3, 5, 2, 7, 5], 1, 5))
print(Solution().countSubarrays([1, 1, 1, 1], 1, 1))
