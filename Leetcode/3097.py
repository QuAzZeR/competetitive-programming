from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        m = 2 * 10**5
        left = 0
        right = 0
        x = 0
        n = len(nums)
        num_digits = 32
        bits = [-1 for i in range(num_digits)]
        if max(nums) >= k:
            return 1
        while right < n:
            x |= nums[right]
            for b in range(num_digits):
                if nums[right] & (1 << b):
                    bits[b] = right
            while x >= k and left <= right:
                m = min(m, right - left + 1)
                for b in range(num_digits):
                    if nums[left] & (1 << b) and bits[b] == left:
                        bits[b] = -1
                        x ^= 1 << b
                left += 1
            right += 1
        if m == (2 * 10**5):
            return -1
        return m


print(Solution().minimumSubarrayLength([1, 2, 3], 2))
print(Solution().minimumSubarrayLength([2, 1, 8], 10))
print(Solution().minimumSubarrayLength([1, 2], 0))
print(Solution().minimumSubarrayLength([32, 2, 24, 1], 35))
print(Solution().minimumSubarrayLength([16, 1, 2, 20, 32], 45))
print(Solution().minimumSubarrayLength([32, 1, 25, 11, 2], 59))
print(Solution().minimumSubarrayLength([1, 12, 26, 2], 8))
