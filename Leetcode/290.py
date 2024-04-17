class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = {}
        w = {}
        words = s.split(" ")
        lp = len(pattern)
        lw = len(words)
        if lp != lw:
            return False
        for i in range(lp):
            if pattern[i] not in p:
                p[pattern[i]] = words[i]
            if p[pattern[i]] != words[i]:
                return False
        for i in range(lw):
            if words[i] not in w:
                w[words[i]] = pattern[i]
            if w[words[i]] != pattern[i]:
                return False
        return True


print(Solution().wordPattern("abba", "dog cat cat dog"))
print(Solution().wordPattern("abbc", "dog cat cat dog"))
print(Solution().wordPattern("abba", "dog cat cat fish"))
print(Solution().wordPattern("aaaa", "dog cat cat dog"))
