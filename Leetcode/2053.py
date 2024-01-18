from typing import Counter, List
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = Counter(arr)
        d = [i for i in d if d[i] == 1]
        c = 1
        for i in arr:
            if i in d:
                if c == k:
                    return i
                c += 1
        return ''
print(Solution().kthDistinct(arr = ["d","b","c","b","c","a"], k = 2))
print(Solution().kthDistinct(arr = ["aaa","aa","a"], k = 1))
print(Solution().kthDistinct(arr = ["a","b","a"], k = 3))
