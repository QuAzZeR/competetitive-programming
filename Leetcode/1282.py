from typing import List
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        answer = []
        g = {}
        for i, v in enumerate(groupSizes):
            if v not in g:
                g[v] = []
            g[v].append(i)
        for i in g:
            if len(g[i]) != i:
                for j in range(0, len(g[i])//i):
                    answer.append(g[i][0+i*j:i+i*j])
            else:
                answer.append(g[i])
        return answer
print(Solution().groupThePeople([3,3,3,3,3,1,3]))
print(Solution().groupThePeople([2,1,3,3,3,2]))
