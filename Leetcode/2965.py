from collections import defaultdict
from typing import List
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        missing = 0
        repeated = 0
        d = defaultdict(int)
        for i in grid:
            for j in i:
                d[j] += 1
                if d[j] == 2:
                    repeated = j
        for i in range(1,n**2+1):
            if i not in d:
                missing = i
                break

        return [repeated, missing]
print(Solution().findMissingAndRepeatedValues([[1,3],[2,2]]))
print(Solution().findMissingAndRepeatedValues([[9,1,7],[8,9,2], [3,4,6]]))

