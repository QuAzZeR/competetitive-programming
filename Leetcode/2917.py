from collections import defaultdict
from typing import List
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        for i in nums:
            x = bin(i).split('b')[1][::-1]
            for j in range(len(x)):
                if x[j] == '1':
                    d[j].append(i)

        return sum([2**i for i in d if len(d[i]) >=k])
print(Solution().findKOr([7,12,9,8,9,15], 4))
print(Solution().findKOr([2,12,1,11,4,5], 6))
print(Solution().findKOr([10,8,5,9,11,6,8], 1))


