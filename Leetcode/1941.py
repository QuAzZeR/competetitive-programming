from collections import defaultdict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = defaultdict(int)
        for i in s:
                d[i] += 1
        m = d[s[0]]
        for i in d:
            if d[i] != m:
                return False
        return True

print(Solution().areOccurrencesEqual("abacbc"))
print(Solution().areOccurrencesEqual("aaabb"))
