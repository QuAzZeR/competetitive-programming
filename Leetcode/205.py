class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            elif s[i] in d and d[s[i]] != t[i]:
                return False
        d = {}
        for i in range(len(s)):
            if t[i] not in d:
                d[t[i]] = s[i]
            elif t[i] in d and d[t[i]] != s[i]:
                return False
        return True


print(Solution().isIsomorphic("egg", "add"))
print(Solution().isIsomorphic("foo", "bar"))
print(Solution().isIsomorphic("paper", "title"))
