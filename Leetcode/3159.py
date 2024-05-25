from typing import List
from collections import Counter


class Solution:
    def occurrencesOfElement(
        self, nums: List[int], queries: List[int], x: int
    ) -> List[int]:
        o = []
        n = len(nums)
        for i in range(n):
            c = nums[i]
            if c == x:
                o.append(i)
        lo = len(o)
        if lo == 0:
            return [-1] * len(queries)
        answer = []
        for i in queries:
            if i > lo:
                answer.append(-1)
            else:
                answer.append(o[i - 1])
        return answer


print(Solution().occurrencesOfElement([1, 3, 1, 7], [1, 3, 2, 4], 1))
print(Solution().occurrencesOfElement([1, 2, 3], [10], 5))
