from typing import List
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        cx,cy = points[0]

        l = len(points)
        idx = 1
        count = 0
        while idx < l:
            x,y = points[idx]
            dx,dy = 0,0
            if cx == x and cy == y:
                idx += 1
                continue
            if cx > x:
                dx = -1
            elif cx < x:
                dx = 1
            if cy > y:
                dy = -1
            elif cy < y:
                dy = 1
            cx += dx
            cy += dy
            count += 1
        return count

print(Solution().minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
print(Solution().minTimeToVisitAllPoints([[3,2],[-2,2]]))
