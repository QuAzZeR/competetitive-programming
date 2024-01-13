from typing import Counter, List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer = 0
        for j in range(len(grid)):
            answer += len(list(filter(lambda x: x < 0, grid[j])))
        return answer
print(Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(Solution().countNegatives([[3,2],[1,0]]))
