class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))

print(Solution().minimizedStringLength("aaabc"))
print(Solution().minimizedStringLength("cbbd"))
print(Solution().minimizedStringLength("dddaaa"))
print(Solution().minimizedStringLength("bb"))
print(Solution().minimizedStringLength("ffs"))
print(Solution().minimizedStringLength("ipi"))
