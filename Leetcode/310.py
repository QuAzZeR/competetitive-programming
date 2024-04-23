from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        p = {i: [] for i in range(n)}
        number_adj = [0] * n
        answer = []
        for s, e in edges:
            p[s].append(e)
            p[e].append(s)
            number_adj[s] += 1
            number_adj[e] += 1
            if len(p[s]) == n - 1:
                answer.append(s)
            if len(p[e]) == n - 1:
                answer.append(e)
        if len(answer) != 0:
            return answer
        answer = deque([i for i in range(n) if len(p[i]) == 1])
        left_node = n
        while left_node > 2:
            left_node -= len(answer)
            for _ in range(len(answer)):
                leaf = answer.popleft()
                for n in p[leaf]:
                    number_adj[n] -= 1
                    if number_adj[n] == 1:
                        answer.append(n)

        return list(answer)


print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
print(Solution().findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
