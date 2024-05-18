class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        m = -1
        for i in range(len(s)):
            c = 0
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if m < c:
                        m = c
                c += 1
        return m


print(Solution().maxLengthBetweenEqualCharacters("aa"))
print(Solution().maxLengthBetweenEqualCharacters("abca"))
print(Solution().maxLengthBetweenEqualCharacters("cbzxy"))
