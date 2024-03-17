class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        r = s[::-1]
        for i in range(0, len(s) - 1):
            if s[i : i + 2] in r:
                return True
        return False


print(Solution().isSubstringPresent("leetcode"))
print(Solution().isSubstringPresent("abcba"))
print(Solution().isSubstringPresent("abcd"))
