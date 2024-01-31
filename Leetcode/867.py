from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        answer = [[matrix[0][i]] for i in range(m)]
        for i in range(m):
            for j in range(1, n):
                answer[i].append(matrix[j][i])
        return answer


print(Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().transpose([[1, 2, 3], [4, 5, 6]]))
