from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        p = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            bricks -= diff
            heapq.heappush(p, diff)
            if bricks < 0:
                bricks += heapq.heappop(p)
                ladders -= 1

            if ladders < 0:
                return i

        return len(heights) - 1


print(Solution().furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1))
print(Solution().furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2))
print(Solution().furthestBuilding([14, 3, 19, 3], 17, 0))
