from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        c = []
        for i in range(n):
            c.append((i, sum(grid[i])))
        c = sorted(c, key=lambda x: (x[1], x[0]))
        return c[-1][0]


print(Solution().findChampion([[0, 1], [0, 0]]))
print(Solution().findChampion([[0, 0, 1], [1, 0, 1], [0, 0, 0]]))
