from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        return (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)


print(Solution().isBoomerang([[1, 1], [2, 3], [3, 2]]))
print(Solution().isBoomerang([[1, 1], [2, 2], [3, 3]]))
print(Solution().isBoomerang([[1, 1], [2, 2], [7, 7]]))
