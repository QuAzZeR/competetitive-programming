from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n + 1):
            c = 0
            for j in range(n):
                if nums[j] >= i:
                    c += 1
                if c > i:
                    break
            if c == i:
                return c
        return -1


print(Solution().specialArray([3, 5]))
print(Solution().specialArray([0, 0]))
print(Solution().specialArray([0, 4, 3, 0, 4]))
