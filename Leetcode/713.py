from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        answer = 0
        m = 1
        left, right = 0, 0
        while right < len(nums):
            m *= nums[right]
            while m >= k:
                m //= nums[left]
                left += 1
            answer += 1 + (right - left)
            right += 1

        return answer


print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))
print(Solution().numSubarrayProductLessThanK([1, 2, 3], 0))
print(
    Solution().numSubarrayProductLessThanK(
        [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19
    )
)
