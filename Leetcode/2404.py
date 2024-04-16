from typing import List
from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        answer = -1
        d = Counter(nums)
        m = 0
        for v, c in sorted(d.items(), key=lambda x: (x[0], x[1])):
            if v % 2 == 0 and m < c:
                m = c
                answer = v
        return answer


print(Solution().mostFrequentEven([0, 1, 2, 2, 4, 4, 1]))
print(Solution().mostFrequentEven([4, 4, 4, 9, 2, 4]))
print(Solution().mostFrequentEven([29, 47, 21, 41, 13, 37, 25, 7]))
