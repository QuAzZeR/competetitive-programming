class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        a = s.count(c)
        if a == 0:
            return 0

        return a * (a + 1) // 2


print(Solution().countSubstrings("abcda", "a"))
print(Solution().countSubstrings("zzz", "z"))
print(Solution().countSubstrings("zzzz", "z"))
