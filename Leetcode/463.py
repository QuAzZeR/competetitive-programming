from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        answer = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    answer += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        answer -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        answer -= 2
        return answer


print(
    Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
)
print(Solution().islandPerimeter([[1]]))
print(Solution().islandPerimeter([[1, 0]]))
