from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        n = len(nums)
        answer = 0
        odd = 0
        cnt = 0
        while r < n:
            if nums[r] % 2 != 0:
                odd += 1
                cnt = 0
            while odd == k:
                if nums[l] % 2 != 0:
                    odd -= 1
                cnt += 1
                l += 1
            answer += cnt
            r += 1
        return answer


print(Solution().numberOfSubarrays([1, 1, 2, 1, 1], 3))
print(Solution().numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
