from collections import defaultdict
from typing import List
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for v,w in items1:
            d[v] += w
        for v,w in items2:
            d[v] += w
        return sorted([[i,d[i]] for i in d], key=lambda x: x[0])

print(Solution().mergeSimilarItems([[1,1],[4,5],[3,8]], [[3,1],[1,5]]))
print(Solution().mergeSimilarItems([[1,1],[3,2],[2,3]], [[2,1],[3,2],[1,3]]))
print(Solution().mergeSimilarItems([[1,3],[2,2]], [[7,1],[2,2],[1,4]]))
