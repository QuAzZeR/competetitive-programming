from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            grid[i][j] = "0"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        no_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    no_islands += 1
                    dfs(i, j)
        return no_islands


print(
    Solution().numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
print(
    Solution().numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
