from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            m_row = min(matrix[i])
            for j in range(m):
                current = matrix[i][j]
                m_column = max([matrix[k][j] for k in range(n)])
                print(current, m_row, m_column)
                if m_row == current and current == m_column:
                    answer.append(current)
        return answer


print(Solution().luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
print(Solution().luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
print(Solution().luckyNumbers([[7, 8], [1, 2]]))
