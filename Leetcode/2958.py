from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = {}
        left = 0
        n = len(nums)
        right = 0
        m = 0
        while right < n:
            r_val = nums[right]
            right += 1
            if r_val not in d:
                d[r_val] = 0
            d[r_val] += 1
            while d[r_val] > k and left < right:
                l_val = nums[left]
                d[l_val] -= 1
                left += 1
            m = max(m, right - left)
        return m


print(Solution().maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2))
print(Solution().maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1))
print(Solution().maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4))
