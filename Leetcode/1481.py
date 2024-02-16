from typing import List
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = Counter(arr)
        a = sorted(d.items(), key=lambda x: x[1])
        l = len(a)
        if k == 0:
            return l

        c = 0
        i = 0
        while i < l:
            if c < k:
                c += a[i][1]
            if c > k:
                break
            i += 1
            if c == k:
                break
        return l - i


print(Solution().findLeastNumOfUniqueInts([5, 5, 4], 1))
print(Solution().findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))
print(Solution().findLeastNumOfUniqueInts([2, 1, 1, 3, 3, 3], 3))
print(Solution().findLeastNumOfUniqueInts([1], 0))
