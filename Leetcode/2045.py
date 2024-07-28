from typing import List
from collections import deque
import unittest


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        g = [[] for _ in range(n+1)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        q = deque([(1,1)])
        d1 = [-1] * (n+1)
        d2 = [-1] * (n+1)
        d1[1] = 0
        while q :
            x, freq = q.popleft()
            t = d1[x] if freq == 1 else d2[x]
            if (t//change)%2 == 1:
                t = change *(t//change + 1) + time
            else:
                t += time
            for i in g[x]:
                if d1[i] == -1:
                    d1[i] = t
                    q.append((i,1))
                elif d2[i] == -1 and d1[i] != t:
                    if i == n:
                        return t
                    d2[i] =t
                    q.append((i,2))
        return 0


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.secondMinimum( n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5), 13)
        self.assertEqual(s.secondMinimum(n = 2, edges = [[1,2]], time = 3, change = 2), 11)


if __name__ == "__main__":
    unittest.main()
