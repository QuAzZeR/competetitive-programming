from typing import List
import unittest


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        grid = [[(i*n) +j for j in range(n)] for i in range(0, n)]
        movement = {
            "RIGHT": [0,1],
            "LEFT": [0, -1],
            "UP": [-1, 0],
            "DOWN": [1, 0]
        }
        x = 0
        y = 0
        for i in commands:
            m = movement[i]
            x += m[0]
            y += m[1]
        return grid[x][y]


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.finalPositionOfSnake(2, ["RIGHT","DOWN"]), 3)
        self.assertEqual(s.finalPositionOfSnake(3,  ["DOWN","RIGHT","UP"]), 1)


if __name__ == "__main__":
    unittest.main()
