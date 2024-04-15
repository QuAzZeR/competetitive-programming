from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        if len(nums) == 2:
            return False
        if len(list(set(nums))) == 1:
            return True
        s = {}
        for i in range(1, len(nums)):
            val = nums[i] + nums[i - 1]
            if val in s:
                return True
            else:
                s[val] = 0
        return False


print(Solution().findSubarrays([4, 2, 4]))
print(Solution().findSubarrays([1, 2, 3, 4, 5]))
print(Solution().findSubarrays([0, 0, 0]))
