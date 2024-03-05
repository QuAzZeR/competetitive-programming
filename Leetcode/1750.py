class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        if s[left] != s[right]:
            return len(s)
        while left < right and s[left] == s[right]:
            c = s[left]
            while left <= right and c == s[left]:
                left += 1
            while left <= right and s[right] == c:
                right -= 1
        return right - left + 1


print(Solution().minimumLength("ca"))
print(Solution().minimumLength("cabaabac"))
print(Solution().minimumLength("aabccabba"))
print(
    Solution().minimumLength(
        "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
    )
)
