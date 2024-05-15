from typing import List
from collections import deque
from heapq import heappop, heappush


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque([])

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    q.append((r, c))
                    grid[r][c] = 0
                else:
                    grid[r][c] = -1

        visited = set()
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:
            for i in range(len(q)):
                x, y = q.popleft()

                if (x, y) in visited:
                    continue

                visited.add((x, y))
                for dx, dy in dir:
                    r, c = x + dx, y + dy
                    if r >= 0 and r < n and c >= 0 and c < n and grid[r][c] == -1:
                        grid[r][c] = grid[x][y] + 1
                        q.append((r, c))

        heap = [(-grid[0][0], 0, 0)]
        answer = grid[0][0]
        visited = set()

        while heap:
            dist, x, y = heappop(heap)
            answer = min(answer, -dist)

            if x == n - 1 and y == n - 1:
                return answer

            if (x, y) in visited:
                continue

            visited.add((x, y))

            for dx, dy in dir:
                r, c = x + dx, y + dy
                if r >= 0 and r < n and c >= 0 and c < n:
                    heappush(heap, (-grid[r][c], r, c))

        return answer


print(Solution().maximumSafenessFactor([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))
print(Solution().maximumSafenessFactor([[0, 0, 1], [0, 0, 0], [0, 0, 0]]))
print(
    Solution().maximumSafenessFactor(
        [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
    )
)
