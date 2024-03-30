from typing import List
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.findAnswer(nums, k) - self.findAnswer(nums, k - 1)

    def findAnswer(self, nums, k):
        answer = 0
        left = 0
        right = 0
        n = len(nums)
        d = {}
        while right < n:
            r_val = nums[right]
            if r_val not in d:
                d[r_val] = 0
            d[r_val] += 1

            while len(d.keys()) > k and left <= right:
                l_val = nums[left]
                d[l_val] -= 1
                if d[l_val] == 0:
                    del d[l_val]
                left += 1

            if len(d.keys()) <= k:
                answer += right - left + 1
            right += 1
        return answer


print(Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
print(Solution().subarraysWithKDistinct([1, 2, 1, 3, 4], 3))
