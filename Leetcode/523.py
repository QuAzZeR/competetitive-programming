from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = 0
        m = {0: -1}
        n = len(nums)
        for i in range(n):
            s += nums[i]
            remain = s % k
            if remain in m:
                if i - m[remain] > 1:
                    return True
            else:
                m[remain] = i
        return False


print(Solution().checkSubarraySum([23, 2, 4, 6, 7], 6))
print(Solution().checkSubarraySum([23, 2, 6, 4, 7], 6))
print(Solution().checkSubarraySum([23, 2, 4, 6, 6], 7))
print(Solution().checkSubarraySum([23, 2, 6, 4, 7], 13))
