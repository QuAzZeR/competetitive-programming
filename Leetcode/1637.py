from typing import List
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: (x[0],x[1]))
        x = [i[0] for i in points]
        answer = 0
        for i in range(1, len(points)):
            diff = x[i] - x[i-1]
            if answer < diff:
                answer = diff
        return answer

print(Solution().maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))
print(Solution().maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
