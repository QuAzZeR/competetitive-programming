class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        return 2


print(Solution().removePalindromeSub("ababa"))
print(Solution().removePalindromeSub("abb"))
print(Solution().removePalindromeSub("baabb"))

print(Solution().removePalindromeSub("bbaabaaa"))
