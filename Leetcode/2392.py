from typing import  List
from collections import defaultdict, deque

import unittest


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def gen(l ):
            d = [0] * k
            o = []
            g = defaultdict(list)
            q = deque()
            for c in l:
                g[c[0] - 1].append(c[1] -1)
                d[c[1] - 1] += 1
            for i in range(k):
                if d[i] == 0:
                    q.append(i)
            while q:
                temp = q.popleft()
                o.append(temp+1)
                for i in g[temp]:
                    d[i] -= 1
                    if d[i] == 0:
                        q.append(i)
            return o

        o1 = gen(rowConditions)
        o2 = gen(colConditions)
        if len(o1) < k or len(o2) < k:
            return []
        m = {o2[i]:i for i in range(k)}
        answer = [[0]  * k for _ in range(k)]
        for i in  range(k):
            answer[i][m[o1[i]]] = o1[i]

        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.buildMatrix(k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]), [[3,0,0],[0,0,1],[0,2,0]])
        self.assertEqual(s.buildMatrix(k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]), [])


if __name__ == "__main__":
    unittest.main()
