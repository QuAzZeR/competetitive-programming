from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        answer = 0
        points = sorted(points, key=lambda x: (x[0], x[1]))
        p = points[0][1]
        for point in points[1:]:
            if p >= point[0]:
                p = min(p, point[1])
            else:
                answer += 1
                p = point[1]
        answer += 1
        return answer


print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
print(Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
print(
    Solution().findMinArrowShots(
        [
            [3, 9],
            [7, 12],
            [3, 8],
            [6, 8],
            [9, 10],
            [2, 9],
            [0, 9],
            [3, 9],
            [0, 6],
            [2, 8],
        ]
    )
)
