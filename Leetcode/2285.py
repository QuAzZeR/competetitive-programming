from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1
        cities = list(range(n))
        cities.sort(key=lambda x: -degree[x])
        answer = 0

        for i in range(n):
            answer += (n - i) * degree[cities[i]]
        return answer


print(Solution().maximumImportance(5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]))
print(Solution().maximumImportance(5, [[0, 3], [2, 4], [1, 3]]))
