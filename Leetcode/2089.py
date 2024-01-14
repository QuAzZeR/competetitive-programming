from collections import defaultdict
from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        s = sorted(nums)
        d = defaultdict(list)
        for i in range(len(s)):
            d[s[i]].append(i)
        return d[target]

print(Solution().targetIndices([1,2,5,2,3], 2))
print(Solution().targetIndices([1,2,5,2,3], 3))
print(Solution().targetIndices([1,2,5,2,3], 5))
