from typing import List
import unittest


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        answer = 0
        n = len(grid)
        m = len(grid[0])
        if n < 3 or m < 3:
            return answer
        def helper(i,j):
            d = [0] * 10
            r = [0] * 3
            c = [0] * 3
            diag1 = 0
            diag2 = 0

            for k in range(i, i + 3):
                for l in range(j, j +3):
                    v = grid[k][l]
                    if v > 9 or v == 0:
                        return False
                    d[v] = 1
                    r[k-i] += v
                    c[l-j] += v
            for k in range(3):
                diag1 += grid[i+k][j+k]
            for k in range(3):
                diag2 += grid[i+2-k][j+2-k]
            for k in range(2):
                if r[k] != r[k+1]:
                    return False
            for k in range(2):
                if c[k] != c[k+1]:
                    return False

            return sum(d) == 9 and (c[0]== diag1) and (r[0] == diag1) and (diag1 == diag2)

        for i in range(n-2):
            for j in range(m - 2):
                if helper(i,j):
                    answer += 1

        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]), 1)
        self.assertEqual(s.numMagicSquaresInside([[8]]), 0)
        self.assertEqual(s.numMagicSquaresInside([[4,7,8],[9,5,1],[2,3,6]]), 0)
        self.assertEqual(s.numMagicSquaresInside([[3,2,1,6],[5,9,6,8],[1,5,1,2],[3,7,3,4]]), 0)


if __name__ == "__main__":
    unittest.main()
