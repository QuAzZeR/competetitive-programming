from typing import List
import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()
        m = []
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(m, -projects[i][1])
                i += 1
            if not m:
                break
            w -= heapq.heappop(m)
        return w


print(Solution().findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]))
print(Solution().findMaximizedCapital(k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2]))
