from typing import List
from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        answer = [0] * n
        c = [1] * n

        def dfs(node, parent):
            for child in g[node]:
                if child != parent:
                    dfs(child, node)
                    c[node] += c[child]
                    answer[node] += answer[child] + c[child]

        def adjust(node, parent):
            for child in g[node]:
                if child != parent:
                    answer[child] = answer[node] - c[child] + (n - c[child])
                    adjust(child, node)

        dfs(0, -1)
        adjust(0, -1)
        return answer


print(Solution().sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
print(Solution().sumOfDistancesInTree(1, []))
print(Solution().sumOfDistancesInTree(2, [[1, 0]]))
