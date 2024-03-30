from typing import List


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)
        possible = [i if i == 1 else -1 for i in possible]
        sum_val = sum(possible)
        # for i in range(n):
        d = possible[0]
        for i in range(1, n):
            if d > sum_val - d:
                return i
            d += possible[i]
        return -1


print(Solution().minimumLevels([1, 0, 1, 0]))
print(Solution().minimumLevels([1, 1, 1, 1, 1]))
print(Solution().minimumLevels([0, 0]))
print(Solution().minimumLevels([1, 1]))
print(Solution().minimumLevels([0, 0, 0]))
