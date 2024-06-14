from typing import List
from collections import Counter


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        x = Counter(nums)
        a = sorted([(i, x[i]) for i in x], key=lambda x: x[0])
        n = len(a)
        p = a[0][0]
        answer = 0
        for i in range(n):
            for j in range(a[i][1]):
                if p >= a[i][0]:
                    answer += p - a[i][0]
                    p += 1
                elif p < a[i][0]:
                    p = a[i][0] + 1

        return answer


print(Solution().minIncrementForUnique([1, 2, 2]))
print(Solution().minIncrementForUnique([3, 2, 1, 2, 1, 7]))
print(Solution().minIncrementForUnique([0, 2, 2]))
