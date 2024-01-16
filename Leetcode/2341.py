from collections import defaultdict
from typing import List
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        count = 0
        for i in nums:
            d[i] += 1

        for i in d:
            count += d[i]//2
            d[i] %= 2
        return [count, sum(d.values())]
print(Solution().numberOfPairs([1,3,2,1,3,2,2]))
print(Solution().numberOfPairs([1,1]))
print(Solution().numberOfPairs([0]))
