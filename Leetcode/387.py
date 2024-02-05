from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        for i in d:
            if d[i] == 1:
                return s.index(i)
        return -1


print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar("aabb"))
