from typing import Counter, List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = Counter(arr)
        return len(set(d.values())) == len(d.values())

print(Solution().uniqueOccurrences([1,2,2,1,1,3]))
print(Solution().uniqueOccurrences([1,2]))
print(Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
