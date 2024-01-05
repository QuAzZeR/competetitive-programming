from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        answer = 0
        count = {}
        n = len(edges)
        for i in edges:
            if i[0] not in count:
                count[i[0]] =0
            count[i[0]] +=1
            if i[1] not in count:
                count[i[1]] =0
            count[i[1]] += 1
        for i in count:
            if count[i] == n:
                answer = i
                break
        return answer

print(Solution().findCenter([[1,2],[2,3],[4,2]]))
print(Solution().findCenter([[1,2],[5,1],[1,3],[1,4]]))

