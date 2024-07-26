from typing import List
import unittest


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        d = [[float('inf')] *n for _ in range(n)]
        for i in range(n):
            d[i][i] = 0

        for u,v,w in edges:
            d[u][v]= w
            d[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i][j] > d[i][k] + d[k][j]:
                        d[i][j] = d[i][k] + d[k][j]

        m = float('inf')
        b = -1
        for i in range(n):
            r  = 0
            for j in range(n):
                if d[i][j] <= distanceThreshold:
                    r += 1
            if r <= m:
                m = r
                b = i
        return b


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4), 3)
        self.assertEqual(s.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2), 0)


if __name__ == "__main__":
    unittest.main()
