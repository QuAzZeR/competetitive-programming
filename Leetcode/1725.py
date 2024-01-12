from typing import List
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        s = [min(i) for i in rectangles]
        m = max(s)
        return s.count(m)

print(Solution().countGoodRectangles([[5,8],[3,9],[5,12],[16,5]]))
print(Solution().countGoodRectangles([[2,3],[3,7],[4,3],[3,7]]))
