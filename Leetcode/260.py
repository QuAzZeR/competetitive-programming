from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        answer = []
        for i in d:
            if d[i] == 1:
                answer.append(i)
        return answer


print(Solution().singleNumber([1, 2, 1, 3, 2, 5]))
print(Solution().singleNumber([-1, 0]))
print(Solution().singleNumber([0, 1]))
