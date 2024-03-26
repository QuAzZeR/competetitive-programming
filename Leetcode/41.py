from typing import List
from collections import Counter


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_value = max(nums)
        if max_value < 0:
            return 1
        d = Counter(nums)
        for i in range(1, max_value + 2):
            if i not in d:
                return i
        return 1


print(Solution().firstMissingPositive([1, 2, 0]))
print(Solution().firstMissingPositive([3, 4, -1, 1]))
print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))
print(Solution().firstMissingPositive([-5]))
