from math import sqrt
from typing import List
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        m = 0
        m_area = 0
        for i in dimensions:
            diagonal = sqrt(i[0]**2+i[1]**2)
            area = i[0]*i[1]
            if m < diagonal:
                m = diagonal
                m_area = area
            elif m ==diagonal:
                if m_area < area:
                    m_area = area
        return m_area

print(Solution().areaOfMaxDiagonal([[9,3],[8,6]]))
print(Solution().areaOfMaxDiagonal([[4,3],[3,4]]))
print(Solution().areaOfMaxDiagonal([[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]]))
