from typing import List
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        d = [[0 for i in range(n)] for j in range(m)]
        for i in indices:
            for j in range(n):
                d[i[0]][j] += 1
            for j in range(m):
                d[j][i[1]] += 1
        answer =  0
        for i in d:
            answer += sum(list(map(lambda x: x%2 != 0, i)))
        return answer


print(Solution().oddCells(2,3,[[0,1],[1,1]]))
print(Solution().oddCells(2,2,[[1,1],[0,0]]))
