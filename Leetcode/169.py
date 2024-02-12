from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        m = 0
        k = None
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
            if d[i] > m:
                m = d[i]
                k = i
        return k


print(Solution().majorityElement([3, 2, 3]))
print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
