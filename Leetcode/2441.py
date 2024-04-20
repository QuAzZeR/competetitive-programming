from typing import List
from collections import Counter


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d = Counter(nums)
        m = float("-inf")
        for i in d:
            if i > 0 and -i in d:
                m = max(m, i)
        return int(m) if m != float("-inf") else -1


print(Solution().findMaxK([-1, 2, -3, 3]))
print(Solution().findMaxK([-1, 10, 6, 7, -7, 1]))
print(Solution().findMaxK([-10, 8, 6, 7, -2, -3]))
