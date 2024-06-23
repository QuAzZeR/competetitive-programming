from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = deque()
        d = deque()
        m = 0
        l = 0
        n = len(nums)
        r = 0
        while r < n:
            while i and nums[r] < i[-1]:
                i.pop()
            i.append(nums[r])
            while d and nums[r] > d[-1]:
                d.pop()
            d.append(nums[r])
            while d[0] - i[0] > limit:
                if nums[l] == i[0]:
                    i.popleft()
                if nums[l] == d[0]:
                    d.popleft()
                l += 1
            m = max(m, r - l + 1)
            r += 1
        return m


print(Solution().longestSubarray([8, 2, 4, 7], 4))
print(Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5))
print(Solution().longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))
