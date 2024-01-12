from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        g = []
        answer = 0
        for i in grid:
            g.append(sorted(i, reverse=True))
        for i in range(len(grid[0])):
            answer += max([g[j][i] for j in range(len(grid))])
        return answer
print(Solution().deleteGreatestValue([[1,2,4],[3,3,1]]))
print(Solution().deleteGreatestValue([[10]]))

