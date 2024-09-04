from typing import List
import unittest


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        answer = 0
        x = 0
        y = 0
        d = 0
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        o = set(map(tuple, obstacles))
        for cmd in commands:
            if cmd == -1:
                d = (d+1)%4
            elif cmd == -2:
                d = (d-1)%4
            else:
                for _ in range(cmd):
                    nx = x+dir[d][0]
                    ny = y+dir[d][1]
                    if (nx, ny) in o:
                        break
                    x = nx
                    y = ny
                    answer = max(answer, x*x + y*y)
                nx = x
                ny = y
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.robotSim([4,-1,3], []), 25)
        self.assertEqual(s.robotSim([4,-1,4,-2,4], [[2,4]]), 65)
        self.assertEqual(s.robotSim([6,-1,-1,6], []), 36)


if __name__ == "__main__":
    unittest.main()
