from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {i[0]:i[1] for i in paths}
        l = len(paths)
        answer = ''
        for i in d:
            current = i
            count = 1
            while current in d:
                if count == l:
                    answer = d[current]
                    break
                current = d[current]
                count += 1
        return answer

print(Solution().destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(Solution().destCity([["B","C"], ["D","B"], ["C", "A"]]))
print(Solution().destCity([["A","Z"]]))
