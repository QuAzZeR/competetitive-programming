from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        m = {
            "B": 1,
            "W": 0,
        }
        for i in range(2):
            for j in range(2):
                s = (
                    m[grid[i][j]]
                    + m[grid[i][j + 1]]
                    + m[grid[i + 1][j]]
                    + m[grid[i + 1][j + 1]]
                )
                if s == 1 or s == 3 or s == 0 or s == 4:
                    return True

        return False


print(Solution().canMakeSquare([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]))
print(Solution().canMakeSquare([["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]]))
print(Solution().canMakeSquare([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "W"]]))
