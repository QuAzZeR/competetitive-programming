from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = set()
        answer = 0

        def dfs(x, y):
            if (
                (x < 0 or x >= n)
                or (y < 0 or y >= m)
                or (x, y) in visited
                or grid[x][y] == 0
            ):
                return 0
            visited.add((x, y))
            left = dfs(x, y - 1)
            right = dfs(x, y + 1)
            up = dfs(x - 1, y)
            down = dfs(x + 1, y)
            visited.remove((x, y))
            return grid[x][y] + max([left, right, up, down])

        for i in range(n):
            for j in range(m):
                if grid[i][j] and (i, j) not in visited:
                    answer = max(answer, dfs(i, j))
        return answer


print(Solution().getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
print(
    Solution().getMaximumGold([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]])
)
