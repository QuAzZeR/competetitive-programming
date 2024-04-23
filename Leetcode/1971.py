from queue import Queue
from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        q = Queue()
        p = {}
        v = set()
        for i in edges:
            s, e = i
            if s not in p:
                p[s] = []
            if e not in p:
                p[e] = []
            p[s].append(e)
            p[e].append(s)
        q.put(source)
        while not q.empty():
            c = q.get()
            if c == destination:
                return True
            if c not in p:
                continue
            for i in p[c]:
                if i == destination:
                    return True
                if i not in v:
                    v.add(i)
                    q.put(i)
        return False


print(Solution().validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
print(Solution().validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))
