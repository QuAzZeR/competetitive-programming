from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        dx, dy = x2 - x1, y2 - y1
        for i in range(2, len(coordinates)):
            x2, y2 = coordinates[i]
            if dx * (y2 - y1) != dy * (x2 - x1):
                return False
        return True


print(Solution().checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(Solution().checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
print(Solution().checkStraightLine([[0, 0], [0, 1], [0, -1]]))
