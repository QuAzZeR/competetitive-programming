from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        answer = []
        m = len(land)
        n = len(land[0])
        self.pos = []

        def finding(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or land[i][j] == 0:
                return
            self.pos.append([i, j])
            land[i][j] = 0
            finding(i, j - 1)
            finding(i, j + 1)
            finding(i - 1, j)
            finding(i + 1, j)

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    self.pos = []
                    finding(i, j)
                    self.pos.sort()
                    fx, fy = self.pos[0]
                    lx, ly = self.pos[-1]
                    answer.append([fx, fy, lx, ly])
        return answer


print(Solution().findFarmland([[1, 0, 0], [0, 1, 1], [0, 1, 1]]))
print(Solution().findFarmland([[1, 1], [1, 1]]))
