from typing import List
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        answer = []
        for i in range(len(grid)-3+1):
            c  = []
            for j in range(len(grid[i])-3 +1):
                m = 0
                for k in range(i,i+3):
                    m  = max([m]+grid[k][j:j+3])
                c.append(m)
            answer.append(c)
        return answer

print(Solution().largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
print(Solution().largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))

