from typing import List
import unittest


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        num_rows = len(rowSum)
        num_cols = len(colSum)

        current_row = 0
        current_column = 0
        answer  = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

        while current_row < num_rows or current_column < num_cols:
            if current_row >= num_rows:
                answer[num_rows - 1][current_column] = colSum[current_column]
                current_column +=1
                continue
            elif current_column >= num_cols:
                answer[current_row][num_cols-1] = rowSum[current_row]
                current_row += 1
                continue
            v = min(rowSum[current_row], colSum[current_column])
            rowSum[current_row] -= v
            colSum[current_column] -= v
            answer[current_row][current_column] = v
            if rowSum[current_row] == 0:
                current_row += 1
            if colSum[current_column] == 0:
                current_column += 1


        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.restoreMatrix([3,8], [4,7]), [[3,0],
         [1,7]])
        self.assertEqual(s.restoreMatrix([5,7,10], [8,6,8]),[[0,5,0],
         [6,1,0],
         [2,0,8]]
)


if __name__ == "__main__":
    unittest.main()
