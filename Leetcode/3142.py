from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        answer = True
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if i + 1 < n and grid[i][j] != grid[i + 1][j]:
                    return False
                if j + 1 < m and grid[i][j] == grid[i][j + 1]:
                    return False
        return answer


print(Solution().satisfiesConditions([[1, 0, 2], [1, 0, 2]]))
print(Solution().satisfiesConditions([[1, 1, 1], [0, 0, 0]]))
print(Solution().satisfiesConditions([[1], [2], [3]]))
