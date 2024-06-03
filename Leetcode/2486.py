class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        m = len(s)
        n = len(t)
        while i < m and j < n:
            if s[i] == t[j]:
                j += 1
            i += 1
        return n - j


print(Solution().appendCharacters("coaching", "coding"))
print(Solution().appendCharacters("abcde", "a"))
print(Solution().appendCharacters("z", "abcde"))
