from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        n = len(wage)
        r = sorted([(wage[i] / quality[i], quality[i]) for i in range(n)])
        qs = 0
        mr = 0.0
        h = []
        for i in range(k):
            mr = max(mr, r[i][0])
            qs += r[i][1]
            heapq.heappush(h, -r[i][1])
        answer = mr * qs

        for i in range(k, n):
            mr = max(mr, r[i][0])
            qs += r[i][1] + heapq.heappop(h)
            heapq.heappush(h, -r[i][1])
            answer = min(answer, mr * qs)
        return answer


print(Solution().mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2))
print(Solution().mincostToHireWorkers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3))
