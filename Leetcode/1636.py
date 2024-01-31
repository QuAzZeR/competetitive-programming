from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = Counter(nums)

        return sorted(nums, key=lambda x: (d[x], -x))


print(Solution().frequencySort([1, 1, 2, 2, 2, 3]))
print(Solution().frequencySort([2, 3, 1, 3, 2]))
print(Solution().frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]))
