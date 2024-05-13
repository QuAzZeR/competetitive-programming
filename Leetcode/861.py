from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        answer = (1 << (m - 1)) * n
        for i in range(1, m):
            val = 1 << (m - 1 - i)
            set_count = 0
            for j in range(n):
                if grid[j][i] == grid[j][0]:
                    set_count += 1
            answer += max(set_count, n - set_count) * val
        return answer


print(Solution().matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
print(Solution().matrixScore([[0]]))
