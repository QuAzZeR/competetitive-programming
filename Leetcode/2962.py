from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        right = 0
        left = 0
        m = max(nums)
        answer = 0
        while right < n:
            if nums[right] == m:
                k -= 1
            right += 1
            while k == 0:
                if nums[left] == m:
                    k += 1
                left += 1
            answer += left
        return answer


print(Solution().countSubarrays([1, 3, 2, 3, 3], 2))
print(Solution().countSubarrays([1, 4, 2, 1], 3))
