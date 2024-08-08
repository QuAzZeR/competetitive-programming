from typing import List
import unittest


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        answer = []
        r =  rStart
        c = cStart

        dr, dc = 0, 1 # directions to move
        t = 2
        moves = 1
        next_moves = 2
        n = rows * cols
        while len(answer) < n:
            if (-1 < r < rows) and ( -1 < c < cols):
                answer.append([r,c])

            r += dr
            c += dc
            moves -= 1
            if moves == 0:
                dr, dc = dc, -dr
                t -= 1
                if t == 0:
                    t = 2
                    moves = next_moves
                    next_moves += 1
                else:
                    moves = next_moves - 1
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.spiralMatrixIII(1,4,0,0), [[0,0],[0,1],[0,2],[0,3]])
        self.assertEqual(s.spiralMatrixIII(5,6,1,4), [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]])


if __name__ == "__main__":
    unittest.main()
