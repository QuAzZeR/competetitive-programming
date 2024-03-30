from typing import List
from collections import Counter


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        concat = []
        for i in nums:
            concat += i
        d = Counter(concat)
        return sorted([i for i in d if d[i] == n])


print(Solution().intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]))
print(Solution().intersection([[1, 2, 3], [4, 5, 6]]))
