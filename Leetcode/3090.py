from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = len(s)
        max_len = 0
        for i in range(l):
            for j in range(i + 1, l + 1):
                c = Counter(s[i:j])
                m = max(c.values())
                if m > 2:
                    continue
                max_len = max(max_len, j - i)
        return max_len


print(Solution().maximumLengthSubstring("bcbbbcba"))
print(Solution().maximumLengthSubstring("aaaa"))
