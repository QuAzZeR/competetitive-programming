from collections import Counter
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        l = len(nums)
        if l % 2 != 0:
            return False

        d = Counter(nums)
        for i in d:
            if d[i] >= 3:
                return False
        return True


print(Solution().isPossibleToSplit([1, 1, 2, 2, 3, 4]))
print(Solution().isPossibleToSplit([1, 1, 1, 1]))
