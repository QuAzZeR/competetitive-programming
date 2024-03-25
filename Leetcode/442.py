from typing import List
from collections import Counter


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        return [i for i in d if d[i] != 1]


print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
print(Solution().findDuplicates([1, 1, 2]))
print(Solution().findDuplicates([1]))
